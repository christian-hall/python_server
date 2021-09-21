# python_server
A script that runs every 15 minutes via crontab for my automated projects

This is meant to run on a Raspberry Pi, or another computer that remains untouched day-to-day

Server day-to-day functions:
1. Logging  - logging.log - notes processes where they occur
2. Error    - logging.err - notes where non-breaking errors occur
3. Critical - critical.err - notes where stack traces print, crashing the code

# eventually Error or Critical errors will generate tickets in a tech support systemz