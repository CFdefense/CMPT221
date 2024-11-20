.. _`Troubleshooting`:

Troubleshooting
===============
This section describes some common issues that can arise and possible solutions.

Issue #1
--------
Not Able to Connect to Database due to port being closed.
Needed to manually start postgres in my terminally everytime on boot, opens port 5432.

Issue #2
--------
Cannot find dependencies needed for the port.
Ensure you are in the correct directory in relation to how you use relative paths within your code.

Issue #3
--------
Correct code but columns do not exist in the database and it is erroring.
Make sure you are clearing the database if you change columns within the schemas.