from collections import Counter

log_list = [None]

log_test = " POWER ON, POWER OFF, IDLE, RUN , POWER OFF, POWER ON, IDLE, RUN , FAULT_1, POWER OFF "

log_list = log_test.split(',')

print(log_list[1])

print(log_list.count(" POWER ON"))