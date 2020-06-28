To-do\'s:

1.  **TODO** add balance workspace test with fixtures and
    fake trees to simulate handling of simple/difficult cases

2.  **TODO** add specific debug script to find sources of
    errors when they do occur

3.  add specific changelog (with versions and updates) and todo\'s file,
    have them for different purposes

4.  try to make refreshing more efficient

Completed:

1.  **DONE** handle extra case where command failed because
    no other container in the direction -\> in that case should break
    loop since this is the wrong direction -\> test script with echoed
    commands in simple cases to see if this makes sense and if this
    stops unnecessary loops

2.  **DONE** modify main to only process if length is
    strictly more than one

3.  **DONE** update git release tag to latest commit after
    makefile

4.  **DONE** add makefile to manage updates to poetry,
    git-tags and AUR, as well as building and publishing -\> make this
    reusable as much as possible and bump to sync everything together
    soon

5.  **DONE** port code-base to aur and make installable to
    bins

6.  **DONE** add instructions to install locally with
    setuptools and wheels

7.  **DONE** update readme and add new gifs for functionatity
    displays -\> try without picom to see if animation looks any better

8.  **DONE** add information about pip, add updated
    information on usage

9.  **DONE** devise failsafe when both booleans are true -\>
    would be necessary for only focused elements

10. **DONE** add variant of script that works only on focused
    elements

11. **DONE** add counters to while and increment end of while
    instead of in for to see actual count

12. **DONE** add failsafe to counter missing data in tree and
    test with logs on empty workspace -\> three edge cases: \[\[\]\],
    \[\], \[Con\] -\> \[Con\] is handled gracefully by
    balance-containers, \[\[\]\] can be filtered out in main and \[\]
    can be prevented during tree construction

13. **DONE** look into problematic tree structure not showing
    depth correctly

14. **DONE** change timeout to 1 second

15. **DONE** port to github and share for feedback

16. **DONE** script exits gracefully even in empty or trivial
    (singular) workspace
