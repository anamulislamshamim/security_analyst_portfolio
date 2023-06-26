#!/usr/bin/env python3
import re

# regex to extract date, time and pid
pattern = r"^\s*(\w{3} \d{1,2} \d{1,2}:\d{2}:\d{2})[\w = \.]*\[(\d+)\]"

# extract data, time and pid and print it
def extract_info(log):
    match = re.findall(pattern, log)
    print("{} pid:{}".format(match[0][0], match[0][1]))


with open("system_log.txt", "r") as f:
    for line in f:
        extract_info(line.strip())