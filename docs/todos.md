To-do\'s:

1.  **TODO** devise failsafe when both booleans are true -\>
    would be necessary for only focused elements

2.  **TODO** add variant of script that works only on focused
    elements

3.  try to make refreshing more efficient

4.  port code-base to pypi to make it more easily installable

Completed:

1.  **DONE** add counters to while and increment end of while
    instead of in for to see actual count

2.  **DONE** add failsafe to counter missing data in tree and
    test with logs on empty workspace -\> three edge cases: \[\[\]\],
    \[\], \[Con\] -\> \[Con\] is handled gracefully by
    balance-containers, \[\[\]\] can be filtered out in main and \[\]
    can be prevented during tree construction

3.  **DONE** look into problematic tree structure not showing
    depth correctly

4.  **DONE** change timeout to 1 second

5.  **DONE** port to github and share for feedback

6.  **DONE** script exits gracefully even in empty or trivial
    (singular) workspace
