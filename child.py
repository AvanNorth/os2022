#!/usr/bin/python

import sys
import os
import time
import random


s_time = sys.argv[1]
s_time = int(s_time)

process_id = os.getpid()
parent_process_id = os.getppid()

print(f"Child [{chld_proc_id}] started. PID {chld_proc_id}. Parent PID {parent_proc_id}")
time.sleep(s_time)
print(f"Child [{chld_proc_id}] ended. PID {chld_proc_id}. Parent PID {parent_proc_id}")

exit_status = random.randint(0, 1)

sys.exit(exit_status)