#!/usr/bin/python

import os
import sys
import random


def chld_run():
    child = os.fork()

    if child == 0:
        argument = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", argument)
    print(f"Parent [{os.getpid()}]: children process with PID {child}")

chld_num = sys.argv[1]
chld_num = int(chld_num)

for i in range(0, chld_num):
    chld_run()

while chld_num > 0:
    child_pid, status = os.wait()
    exit_status = exit_status / 256
    exit_status = int(exit_status)

    print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit status {exit_status}.")
    if exit_status == 0:
        chld_num = chld_num - 1
    else:
        chld_run()