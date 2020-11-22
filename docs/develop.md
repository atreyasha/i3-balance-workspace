## Table of Contents
-   [Tasks](#tasks)
-   [Completed](#completed)

### Tasks

1.  Current

    1.  clean code structure for repository

    2.  loosen i3ipc version bound to allow more generous installations

    3.  add balance workspace test with fixtures and fake trees to
        simulate handling of simple/difficult cases, separate tests for
        gaps and non-gaps, add test dependencies such as pytest and
        Xvfb, try to capture various aspects by emulating python-i3ipc

    4.  look into more efficient workspace tree refreshing with
        connection to private i3ipc sync function

2.  Long-term

    1.  replace while loop with deterministic for loop in recursive
        adjustment where the effect of each size change is checked next
        to adjacent window and this is done until no negative size
        effects are found -\> essentially pre-empt the \"cannot resize\"
        error by checking these sizes beforehand to prevent loss of some
        windows -\> useful for edge cases where windows are made so
        small that they get corrupted, \"cannot resize\" seems to kick
        in after erroneous resizes in some cases which allows for
        negative dimensions

    2.  add specific debug script to find sources of errors when they do
        occur

    3.  think about new features such as balance vertical/horizontal

    4.  add specific changelog (with versions and updates) and todo\'s
        file, have them for different purposes

### Completed

1.  **DONE** remove src directory nesting and keep it direct

    **CLOSED:** *\[2020-11-21 Sat 19:23\]*

2.  **DONE** no percentage change check seems to be causing
    errors as well -\> or possibly return diff and ensure diff was not
    zero

    **CLOSED:** *\[2020-07-03 Fri 22:30\]*

3.  **DONE** handle extra case where command failed because
    no other container in the direction -\> in that case should break
    loop since this is the wrong direction -\> test script with echoed
    commands in simple cases to see if this makes sense and if this
    stops unnecessary loops

    **CLOSED:** *\[2020-06-28 Sun 13:02\]*

4.  **DONE** modify main to only process if length is
    strictly more than one

    **CLOSED:** *\[2020-06-28 Sun 13:02\]*

5.  **DONE** update git release tag to latest commit after
    makefile

    **CLOSED:** *\[2020-06-26 Fri 14:32\]*

6.  **DONE** add makefile to manage updates to poetry,
    git-tags and AUR, as well as building and publishing -\> make this
    reusable as much as possible and bump to sync everything together
    soon

    **CLOSED:** *\[2020-06-26 Fri 14:32\]*

7.  **DONE** port code-base to aur and make installable to
    bins

    **CLOSED:** *\[2020-06-24 Wed 23:32\]*

8.  **DONE** add instructions to install locally with
    setuptools and wheels

    **CLOSED:** *\[2020-06-24 Wed 20:35\]*

9.  **DONE** update readme and add new gifs for functionatity
    displays -\> try without picom to see if animation looks any better

    **CLOSED:** *\[2020-06-24 Wed 20:35\]*

10. **DONE** add information about pip, add updated
    information on usage

    **CLOSED:** *\[2020-06-24 Wed 20:35\]*

11. **DONE** devise failsafe when both booleans are true -\>
    would be necessary for only focused elements

    **CLOSED:** *\[2020-06-24 Wed 15:21\]*

12. **DONE** add variant of script that works only on focused
    elements

    **CLOSED:** *\[2020-06-24 Wed 15:21\]*

13. **DONE** add counters to while and increment end of while
    instead of in for to see actual count

    **CLOSED:** *\[2020-06-23 Tue 12:30\]*

14. **DONE** add failsafe to counter missing data in tree and
    test with logs on empty workspace -\> three edge cases: \[\[\]\],
    \[\], \[Con\] -\> \[Con\] is handled gracefully by
    balance-containers, \[\[\]\] can be filtered out in main and \[\]
    can be prevented during tree construction

    **CLOSED:** *\[2020-06-23 Tue 12:30\]*

15. **DONE** look into problematic tree structure not showing
    depth correctly

    **CLOSED:** *\[2020-06-23 Tue 11:46\]*

16. **DONE** change timeout to 1 second

    **CLOSED:** *\[2020-06-23 Tue 13:25\]*

17. **DONE** port to github and share for feedback

    **CLOSED:** *\[2020-06-22 Mon 22:28\]*

18. **DONE** script exits gracefully even in empty or trivial
    (singular) workspace

    **CLOSED:** *\[2020-06-23 Tue 01:50\]*