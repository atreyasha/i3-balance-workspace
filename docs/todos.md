To-do\'s:

1.  **TODO** port code-base to aur and make installable to
    bins

2.  **TODO** add makefile to manage updates to poetry,
    git-tags and AUR, as well as building and publishing

3.  add balance workspace test with fixtures and fake trees etc

4.  try to make refreshing more efficient

Completed:

1.  **DONE** add instructions to install locally with
    setuptools and wheels

2.  **DONE** update readme and add new gifs for functionatity
    displays -\> try without picom to see if animation looks any better

3.  **DONE** add information about pip, add updated
    information on usage

4.  **DONE** devise failsafe when both booleans are true -\>
    would be necessary for only focused elements

5.  **DONE** add variant of script that works only on focused
    elements

6.  **DONE** add counters to while and increment end of while
    instead of in for to see actual count

7.  **DONE** add failsafe to counter missing data in tree and
    test with logs on empty workspace -\> three edge cases: \[\[\]\],
    \[\], \[Con\] -\> \[Con\] is handled gracefully by
    balance-containers, \[\[\]\] can be filtered out in main and \[\]
    can be prevented during tree construction

8.  **DONE** look into problematic tree structure not showing
    depth correctly

9.  **DONE** change timeout to 1 second

10. **DONE** port to github and share for feedback

11. **DONE** script exits gracefullf even in empty or trivial
    (singular) workspace
