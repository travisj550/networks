#Socket client example in python
#test 
import socket   #for sockets
import sys  #for exit
import time
import asyncio
import threading
from _thread import *

times = []
#----------------------sends and recieves from server
def send(input):
	try :
		#Set the whole string
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host , port))
		start = time.time()
		s.sendall(str(input).encode())
	except socket.error:
		#Send failed
		print ('Send failed')
		sys.exit()
	
	#print ('Message send successfully')
	
	#Now receive data
	reply = s.recv(20000)
	end = time.time()
	times.append(end-start)
	print (str(len(times)) + ": " + str(end-start))
	s.close()

#----------------------total of send times
def total():
	x = 0
	for i in times:
		x += i
	return x


#create an INET, STREAMing socket
#try:
#   
#except socket.error:
#    print ('Failed to create socket')
#    sys.exit()

#print ('Socket Created')


#-----------------------user inputs
inputHost = input("IP to connect: ")
inputPort = input("Port to connect: ")

host = str(inputHost)
port = int(inputPort)

print ('Socket Connected to ' + host)
print("1: Date and Time \n2: Uptime \n3: Memory Use \n4: Netstat \n5: Current Users \n6: Running Processes \n7: Print total and average turn-around times")
while True: 
	print('Enter an option: ')
	selection = int(input())
	print("How many client requests to generate: ")
	numRequest = int(input())

	if(selection >= 1 and selection <= 6):
		threads = []
		for x in range(int(numRequest)):
			t = threading.Thread(target=send, args=(selection,))
			threads.append(t)
		for x in threads:
			x.start()
		for x in threads:
			x.join()
		print("Total turn-around times: " + str(total()) )
		print("Average turn-around time: " + str(total()/len(times)))
		print("Number of completed requests: " + str(len(times)))


	else:
		print("Total turn-around times: " + str(total()) )
		print("Average turn-around time: " + str(total()/len(times)))
		print("Number of completed requests: " + str(len(times)))
		break


#message.encode(encoding='UTF-8')


