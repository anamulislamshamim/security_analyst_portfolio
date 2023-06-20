#!/usr/bin/env python3

# import the necessary modules
import shutil
import psutil


# check if the free disk minimum 20 %
def check_disk_usage(disk):
    du = shutil.disk_usage("/")
    return (du.free / du.total * 100) >= 20


# check if the cpu usages less than 75% per second
def check_cpu_usage():
    return psutil.cpu_percent(1) < 75


# show the notification: if disk space free more than 20 percent and cpu usages less than 75 percent per second then print system is healthy
# otherwise print "Error: disk usages more than 20% and cpu usages more than 75%"

if not check_disk_usage("/") and not check_cpu_usage():
    print("Error: disk usages more than 20% and cpu usages more than 75%")
else:
    print("Healthy: System is 100 percent ok🤗")


