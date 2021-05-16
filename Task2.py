"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def getLongestCall():
    differentCalls = {}
    for index in range(1, len(calls)):
        callerNumber = calls[index][0]
        receivingNumber = calls[index][1]
        callDuration = int(calls[0][-1])

        if callerNumber in differentCalls:
            differentCalls[callerNumber] += callDuration
        else:
            differentCalls[callerNumber] = callDuration
        if receivingNumber in differentCalls:
            differentCalls[receivingNumber] += callDuration
        else:
            differentCalls[receivingNumber] = callDuration
    maxCall = 0
    num = 0

    for item in differentCalls.items():
        if item[1] > maxCall:
            maxCall = item[1]
            num = item[0]
    print(f"{num} spent the longest time, {maxCall} seconds, on the phone during September 2016.")


getLongestCall()
