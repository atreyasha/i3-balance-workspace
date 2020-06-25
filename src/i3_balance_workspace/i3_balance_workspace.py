#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import i3ipc
from typing import List, Dict
from argparse import ArgumentParser
from .utils import arg_metav_formatter, timeout


def refresh_workspace() -> i3ipc.Con:
    """
    Function refreshes i3 connection and returns the latest workspace container

    Returns:
        workspace (i3ipc.Con): workspace container
    """
    i3 = i3ipc.Connection()
    if SCOPE == "workspace":
        workspace = i3.get_tree().find_focused().workspace()
    elif SCOPE == "focus":
        workspace = i3.get_tree().find_focused()
    return workspace


def adjust_container(container: i3ipc.Con, ideal_dim: float,
                     direction: str) -> i3ipc.CommandReply:
    """
    Function to deterministically adjust a single container

    Args:
        container (i3ipc.Con): i3ipc.Container to adjust
        ideal_dim (float): Target dimension in pixels
        direction (str): Direction in which growing/shrinking should happen

    Returns:
        msg (str): Command sent out to i3
        reply (i3ipc.CommandReply): Reply of resizing command given to i3
    """
    current_dims = [container.rect.width, container.rect.height]
    if direction == "width":
        diff = ideal_dim - current_dims[0]
        if diff >= 0:
            msg = "resize grow right %d px" % diff
        else:
            msg = "resize shrink right %d px" % abs(diff)
    elif direction == "height":
        diff = ideal_dim - current_dims[1]
        if diff >= 0:
            msg = "resize grow down %d px" % diff
        else:
            msg = "resize shrink down %d px" % abs(diff)
    reply = container.command(msg)
    return msg, reply


def recursive_adjustment(containers: List[i3ipc.Con], ids: List[int],
                         dim: str) -> List[i3ipc.Con]:
    """
    Function to recursively adjust list of containers at a given tree level

    Args:
        containers (List[i3ipc.Con]): List of containers to recursively adjust
        ids (List[int]): List of id's of respective containers
        dim (str): Which dimension to address during adjustment

    Returns:
        containers (List[i3ipc.Con]): Update list of containers for other
        processes to refer back to
    """
    redo = True
    counter = 0
    ideal_dim = (
        sum([getattr(container.rect, dim)
             for container in containers]) / len(containers))
    while redo and counter < (len(containers) - 1):
        redo = False
        for i in range(len(containers) - 1):
            initial_sample_percentage = containers[i].percent
            msg, reply = adjust_container(containers[i], ideal_dim, dim)
            workspace = refresh_workspace()
            containers = [workspace.find_by_id(ID) for ID in ids]
            if reply[0].error is not None:
                if reply[0].error == "Cannot resize.":
                    redo = True
            elif reply[0].success and initial_sample_percentage == containers[
                    i].percent:
                redo = False
                if "grow" in msg:
                    opp_msg = msg.replace("grow", "shrink")
                elif "shrink" in msg:
                    opp_msg = msg.replace("shrink", "grow")
                containers[i].command(opp_msg)
                workspace = refresh_workspace()
                containers = [workspace.find_by_id(ID) for ID in ids]
                break
        counter += 1
    return containers


def balance_containers(containers: List[i3ipc.Con]) -> None:
    """
    Function to balance list of containers

    Args:
        containers (List[i3ipc.Con]): List of containers to recursively adjust
    """
    ids = [container.id for container in containers]
    adjust_heights = not all(container.rect.height == containers[0].rect.height
                             for container in containers)
    adjust_widths = not all(container.rect.width == containers[0].rect.width
                            for container in containers)
    if adjust_widths:
        containers = recursive_adjustment(containers, ids, "width")
    if adjust_heights:
        containers = recursive_adjustment(containers, ids, "height")


def traverse_workspace(
        workspace: i3ipc.Con) -> Dict[int, List[List[i3ipc.Con]]]:
    """
    Function to traverse and parse the workspace tree by level

    Args:
        workspace (i3ipc.Con): Workspace container

    Returns:
        level_nodes (Dict[int, List[List[i3ipc.Con]]]): Dictionary mapping of
        workspace tree
    """
    node_collection = workspace.nodes
    level_nodes = {0: [node_collection]}
    i = 1
    while True:
        node_collection = [
            node.nodes for node_list in level_nodes[i - 1]
            for node in node_list if len(node.nodes) > 0
        ]
        if len(node_collection) > 0:
            level_nodes[i] = node_collection
            if any(
                    len(node.nodes) > 0 for node_list in level_nodes[i]
                    for node in node_list):
                i += 1
            else:
                break
        else:
            break
    return level_nodes


def main() -> None:
    """
    Main function to balance i3 window sizes with timeout as failsafe
    in case of problematic recursions or stale windows
    """
    parser = ArgumentParser(formatter_class=arg_metav_formatter)
    parser.add_argument("--scope",
                        type=str,
                        default="workspace",
                        choices=["workspace", "focus"],
                        help="scope of resizing containers")
    parser.add_argument("--timeout",
                        type=int,
                        default=1,
                        help="timeout in seconds for resizing")
    args = parser.parse_args()
    global SCOPE
    SCOPE = args.scope
    workspace = refresh_workspace()
    workspace_tree = traverse_workspace(workspace)
    with timeout(seconds=args.timeout):
        for i in sorted(workspace_tree.keys(), reverse=True):
            for j in range(len(workspace_tree[i])):
                containers = workspace_tree[i][j]
                containers = [
                    container for container in containers
                    if container.rect.width <= workspace.rect.width
                    and container.rect.height <= workspace.rect.height
                ]
                if len(containers) > 0:
                    balance_containers(containers)
                    workspace = refresh_workspace()
                    workspace_tree = traverse_workspace(workspace)


if __name__ == "__main__":
    main()
