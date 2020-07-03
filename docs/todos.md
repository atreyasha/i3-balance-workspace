To-do\'s:

1.  **TODO** add balance workspace test with fixtures and
    fake trees to simulate handling of simple/difficult cases, separate
    tests for gaps and non-gaps, add test dependencies such as pytest
    and Xvfb, try to capture various aspects

2.  **TODO** replace while loop with deterministic for loop
    in recursive adjustment where the effect of each size change is
    checked next to adjacent window and this is done until no negative
    size effects are found -\> essentially pre-empt the \"cannot
    resize\" error by checking these sizes beforehand to prevent loss of
    some windows -\> useful for edge cases where windows are made so
    small that they get corrupted, \"cannot resize\" seems to kick in
    after erroneous resizes in some cases which allows for negative
    dimensions

3.  **TODO** add specific debug script to find sources of
    errors when they do occur

4.  add specific changelog (with versions and updates) and todo\'s file,
    have them for different purposes

5.  try to make refreshing more efficient, perhaps with connection
    private i3ipc sync function

Completed:

1.  **DONE** no percentage change check seems to be causing
    errors as well -\> or possibly return diff and ensure diff was not
    zero

2.  **DONE** handle extra case where command failed because
    no other container in the direction -\> in that case should break
    loop since this is the wrong direction -\> test script with echoed
    commands in simple cases to see if this makes sense and if this
    stops unnecessary loops

3.  **DONE** modify main to only process if length is
    strictly more than one

4.  **DONE** update git release tag to latest commit after
    makefile

5.  **DONE** add makefile to manage updates to poetry,
    git-tags and AUR, as well as building and publishing -\> make this
    reusable as much as possible and bump to sync everything together
    soon

6.  **DONE** port code-base to aur and make installable to
    bins

7.  **DONE** add instructions to install locally with
    setuptools and wheels

8.  **DONE** update readme and add new gifs for functionatity
    displays -\> try without picom to see if animation looks any better

9.  **DONE** add information about pip, add updated
    information on usage

10. **DONE** devise failsafe when both booleans are true -\>
    would be necessary for only focused elements

11. **DONE** add variant of script that works only on focused
    elements

12. **DONE** add counters to while and increment end of while
    instead of in for to see actual count

13. **DONE** add failsafe to counter missing data in tree and
    test with logs on empty workspace -\> three edge cases: \[\[\]\],
    \[\], \[Con\] -\> \[Con\] is handled gracefully by
    balance-containers, \[\[\]\] can be filtered out in main and \[\]
    can be prevented during tree construction

14. **DONE** look into problematic tree structure not showing
    depth correctly

15. **DONE** change timeout to 1 second

16. **DONE** port to github and share for feedback

17. **DONE** script exits gracefully even in empty or trivial
    (singular) workspace
