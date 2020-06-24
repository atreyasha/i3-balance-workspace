To-do\'s:

1.  **TODO** add makefile to manage updates to poetry,
    git-tags and AUR

2.  **TODO** port code-base to pypi/aur and make installable
    to bins, add information on OS and compatibility

3.  **TODO** update readme and add new gifs for functionatity
    displays -\> add information about pip and aur installations, add
    information about i3-gaps and extra pipelines

4.  add balance~w~ rkspace test with fixtures and fake trees etc

5.  try to make refreshing more efficient

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
