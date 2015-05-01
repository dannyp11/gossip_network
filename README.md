# gossip_network (Python 2 algorithm)

#Task: 
We have a network of people that can relay the message to those they have connection with.
Assume there is no loop or closed network. After each hour a person will send the message to people they know.

Given a list of people connection, find the least amount of hours needed so that the whole network will get the message.

For example:
Input file gives:
0-1 
1-2
1-4
2-3
4-5
4-6

These lines define these connections. i.e. 0 knows 1, 1 knows 0,2 and 4, 2 knows 3, etc.

The answer for this network is 2 hours (started at person 1)

There are several input files uploaded to test this algorithm, no problem so far.
 
