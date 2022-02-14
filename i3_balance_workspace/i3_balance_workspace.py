#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .utils import ArgparseFormatter, Timeout
from typing import List, Dict, Tuple
from argparse import ArgumentParser
import i3ipc


def refresh_workspace() -> i3ipc.Con:
    """
    Function refreshes i3 connection and returns the latest workspace container

    Returns:
        workspace (i3ipc.Con): workspace container
    """
    # Retrieve i3 connection
    i3 = i3ipc.Connection()
    # Depending on desired scope, get workspace or focused container
    if SCOPE == "workspace":  # type: ignore
        workspace = i3.get_tree().find_focused().workspace()
    elif SCOPE == "focus":  # type: ignore
        workspace = i3.get_tree().find_focused()
    return workspace


def adjust_container(container: i3ipc.Con, ideal_dim: float,
                     direction: str) -> Tuple[str, i3ipc.CommandReply, float]:
    """
    Function to deterministically adjust a single container

    Args:
        container (i3ipc.Con): i3ipc.Container to adjust
        ideal_dim (float): Target dimension in pixels
        direction (str): Direction in which growing/shrinking should happen

    Returns:
        msg (str): Command sent out to i3
        reply (i3ipc.CommandReply): Reply of resizing command given to i3
        diff (float): Difference metric applied in resizing
    """
    # Retrieve dimensions of provided container
    current_dims = [container.rect.width, container.rect.height]
    # Adjust containers by either resizing rightwards or downwards
    # since i3 tree layout provides containers from left to right
    # and consequently from upwards to downwards
    if direction == "width":
        # If width is to be adjusted, compute difference and adjust
        diff = ideal_dim - current_dims[0]
        if diff >= 0:
            msg = "resize grow right %d px" % diff
        else:
            msg = "resize shrink right %d px" % abs(diff)
    elif direction == "height":
        # If height is to be adjusted, compute difference and adjust
        diff = ideal_dim - current_dims[1]
        if diff >= 0:
            msg = "resize grow down %d px" % diff
        else:
            msg = "resize shrink down %d px" % abs(diff)
    # Capture the reply of the command to check success
    reply = container.command(msg)
    # Return both reply and the actual message, in case an error occurs
    return msg, reply, diff


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
    # Based on the number of containers, compute the ideal balanced dimension
    ideal_dim = (
        sum([getattr(container.rect, dim)
             for container in containers]) / len(containers))
    # Errors can occur when expanding one container so much that another
    # container loses too much of its own size. In order to deal with such
    # cases we need to adjust the containers recursively until the ideal
    # dimension differences smooth out and the errors stop
    while redo and counter < (len(containers) - 1):
        redo = False
        # Loop through i3 tree left-to-right and top-to-bottom.
        # We only need to adjust the first N-1 containers since
        # the last container will be automatically adjusted to fill
        # up the remaining gaps
        for i in range(len(containers) - 1):
            # Compute the initial percentage to ensure successful adjustment
            # is indeed meaningful and not an illusion
            initial_sample_percentage = containers[i].percent
            # Adjust the container and retrieve message/reply
            msg, reply, diff = adjust_container(containers[i], ideal_dim, dim)
            # Refresh the workspace and containers to get updated data
            workspace = refresh_workspace()
            containers = [workspace.find_by_id(ID) for ID in ids]
            # Check for errors and decide how to handle them
            if reply[0].error is not None:
                if reply[0].error == "Cannot resize.":
                    # This error means the current container is encroaching too
                    # much into the adjacent container and therefore the resize
                    # operation is being blocked. The only option is to
                    # continue resizing the next containers and redo the
                    # resize operation on this container
                    redo = True
                elif reply[
                        0].error == "No second container found in this direction.":
                    # Due to possible errors with gaps, containers are adjusted
                    # in meaningless directions, which should be stopped
                    redo = False
                    break
            elif reply[0].success and initial_sample_percentage == containers[
                    i].percent and int(diff) != 0:
                # Although sucessful, the container's percentage didn't change.
                # This error arises mainly in i3-gaps where a container is
                # erroneously adjusted in a direction where it would not need
                # to be adjusted without gaps. Essentially gaps contribute to
                # some misleading dimensions which cause this problem.
                # This segment tries to undo adjustment when this error happens
                # and then attempts to exit this entire recursive loop
                redo = False
                # Here we reverse the wrong adjustment message
                if "grow" in msg:
                    opp_msg = msg.replace("grow", "shrink")
                elif "shrink" in msg:
                    opp_msg = msg.replace("shrink", "grow")
                # Execute the reverse message
                containers[i].command(opp_msg)
                # Return the new containers and their states
                workspace = refresh_workspace()
                containers = [workspace.find_by_id(ID) for ID in ids]
                # Break for-loop and consequently gracefully exit while-loop
                break
        counter += 1
    return containers


def balance_containers(containers: List[i3ipc.Con]) -> None:
    """
    Function to balance list of containers

    Args:
        containers (List[i3ipc.Con]): List of containers to recursively adjust
    """
    # Capture the ids of the relevant containers to re-use later
    ids = [container.id for container in containers]
    # Check if all containers have the same heights and widths.
    # If either heights or widths differ, create a boolean to adjust them.
    # Ideally (on i3 without gaps), only either adjust_heights or adjust_widths
    # should be 'True'. However, on i3-gaps both can be 'True' beacuse of
    # issues related to dimension computation with the presence of gaps.
    # We deal with this edge case in i3-gaps by adding an error catcher in
    # `recursive_adjustment`
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
    # Here, we simply expand the workspace tree until we hit the terminal
    # nodes. Along the way, we store all nodes at each level of the tree
    while True:
        node_collection = [
            node.nodes for node_list in level_nodes[i - 1]
            for node in node_list if len(node.nodes) > 0
        ]
        if len(node_collection) > 0:
            # This is to ensure no empty lists are appended, otherwise break
            level_nodes[i] = node_collection
            if any(
                    len(node.nodes) > 0 for node_list in level_nodes[i]
                    for node in node_list):
                # If any nodes appended have child nodes, keep expanding.
                # If not, break this while-loop
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
    # Parse arguments
    parser = ArgumentParser(formatter_class=ArgparseFormatter)
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
    # Create a global SCOPE variable which will be re-used by
    # the `refresh_workspace` function. Global variable is used
    # here to mitigate passing this variable to many functions
    # repeatedly
    global SCOPE
    SCOPE = args.scope  # type: ignore
    # Generate workspace and tree
    workspace = refresh_workspace()
    workspace_tree = traverse_workspace(workspace)
    # Add a timer here to prevent any edge-case problematic recursions
    with Timeout(seconds=args.timeout):
        for i in sorted(workspace_tree.keys(), reverse=True):
            # Start processing workspace tree bottom-up
            for j in range(len(workspace_tree[i])):
                # Go through lists of containers one-by-one
                containers = workspace_tree[i][j]
                # In rare cases where a user mistakenly makes one container
                # too small, this container encounters an error and appears to
                # have a width or height dimension that exceeds that of the
                # workspace it inhabits. This is a logical error and such
                # containers are simply filtered out and ignored
                containers = [
                    container for container in containers
                    if container.rect.width <= workspace.rect.width
                    and container.rect.height <= workspace.rect.height
                ]
                if len(containers) > 1:
                    # Only proceed with balancing if there are more than one
                    # meainingful containers to actually balance
                    balance_containers(containers)
                    # Refresh the workspace and workspace tree
                    # so that this variable can be re-used dynamically
                    # in this for-loop
                    workspace = refresh_workspace()
                    workspace_tree = traverse_workspace(workspace)


if __name__ == "__main__":
    main()
