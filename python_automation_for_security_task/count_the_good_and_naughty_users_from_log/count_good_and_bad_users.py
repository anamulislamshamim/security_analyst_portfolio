#!/usr/bin/env python3

import re
import sys


# store the log_file from the command line
log_file = sys.argv[1]
# regex to search the username in log
pattern = r"USER \((\w+)\)"

# count the user name and store it into the dictionary
usernames = {}

# open the log file and read every line and count the username
with open(log_file) as f:
    for line in f:
        # if the line does not contain cron just jump to next line
        if 'CRON' not in line:
            continue
        # search the name and store value in result variable
        result = re.search(pattern, line)
        # if result is none then jump the next line
        if result is None:
            continue
        # store username in name variable
        name = result[1]
        # increment the value
        usernames[name] = usernames.get(name, 0) + 1


# print the result dictionary
print(usernames)


