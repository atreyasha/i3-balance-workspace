To-do\'s:

1.  **TODO** update readme and add new gifs for functionatity
    displays -\> try without picom to see if animation looks any better

2.  **TODO** add information about pip, add updated
    information on usage

3.  **TODO** add instructions to install locally with
    setuptools and wheels

4.  **TODO** port code-base to aur and make installable to
    bins

5.  **TODO** add makefile to manage updates to poetry,
    git-tags and AUR, as well as building and publishing

6.  add balance workspace test with fixtures and fake trees etc

7.  try to make refreshing more efficient

Completed:

1.  **DONE** devise failsafe when both booleans are true -\>
    would be necessary for only focused elements

2.  **DONE** add variant of script that works only on focused
    elements

3.  **DONE** add counters to while and increment end of while
    instead of in for to see actual count

4.  **DONE** add failsafe to counter missing data in tree and
    test with logs on empty workspace -\> three edge cases: \[\[\]\],
    \[\], \[Con\] -\> \[Con\] is handled gracefully by
    balance-containers, \[\[\]\] can be filtered out in main and \[\]
    can be prevented during tree construction

5.  **DONE** look into problematic tree structure not showing
    depth correctly

6.  **DONE** change timeout to 1 second

7.  **DONE** port to github and share for feedback

8.  **DONE** script exits gracefullf even in empty or trivial
    (singular) workspace
