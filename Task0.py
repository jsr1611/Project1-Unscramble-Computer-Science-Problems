"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def getTextRecord(index):
    msg = f"First record of texts, {texts[index][0]} texts {texts[index][1]} at time {texts[index][-1]}"
    return msg


def getCallRecord(index):
    msg = f"Last record of calls, {calls[index][0]} calls {calls[index][1]} at time {calls[index][2]}, lasting {calls[index][-1]} seconds"
    return msg


print(getTextRecord(0))
print(getCallRecord(-1))
