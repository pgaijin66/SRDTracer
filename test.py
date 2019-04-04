from pprint import pprint as pp
import sys

file_name=sys.argv[1]
dsdv_trace = open(file_name,'r')
send_count = 0
received_count = 0
list_trace = []
line_count = 0
dropped_count = 0

for line in dsdv_trace:
	list_trace.append(line)
	line_count += 1
	
for i in range(line_count):
	if((list_trace[i].split(' '))[0] == 's'):
		send_count += 1
	elif((list_trace[i].split(' '))[0] == 'r'):
		received_count += 1
	elif((list_trace[i].split(' '))[0] == 'D'):
		dropped_count += 1
	else:
		pass
	 
pp('Number of packets sent: {}'.format(send_count))
pp('Number of packet received: {}'.format(received_count))
pp('Number of packet dropped: {}'.format(dropped_count))
pp('Simulation time: {} ms'.format((list_trace[-1].split(' ')[1])))
