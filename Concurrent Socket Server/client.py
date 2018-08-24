#Socket client example in python
#test 
import socket   #for sockets
import sys  #for exit
import time
import csv
from multiprocessing import *

#times = []

def total(return_dict):
	x=0
	for i in range(len(return_dict)):
		x += return_dict[i]
		#print("round " + str(i) + ": " + str(return_dict[i]))
	return x


#----------------------sends and recieves from server
def send(input, return_dict, procnum):
	try :
		#Set the whole string
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host , port))
		start = time.time()
		#print ("Start " + str(procnum) + ": " + str(start))
		s.sendall(str(input).encode())
	except socket.error:
		#Send failed
		print ('Send failed')
		sys.exit()
	
	#print ('Message send successfully')
	
	#Now receive data
	reply = s.recv(1024)

	#print(str(reply))

	end = time.time()
	#times.append(end-start)
	return_dict[procnum] = end-start
	#print ("End " + str(procnum) + ": " + str(end))

	i=0
	with open('data.csv', 'a', newline='')as c:
		data = csv.writer(c)
		data.writerow([procnum, end-start])
		i+=1

	s.close()
	print ("Process " + str(procnum) + ": " + str(end-start))


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
	print("How many tests to run: ")
	test = int(input())

	with open('data.csv', 'w', newline='')as a:
		main = csv.writer(a)
		main.writerow(['number', 'time'])

	for z in range(test):
		if(selection >= 1 and selection <= 6):

			manager = Manager()
			return_dict = manager.dict()

			processes = []

			start = time.time()

			for x in range(int(numRequest)):
				t = Process(target=send, args=(selection,return_dict,x))
				processes.append(t)
			for x in processes:
				x.start()
			for x in processes:
				x.join()

			end = time.time()
			
			print("Total turn-around time: " + str(end-start))
			print("Average turn-around time: " + str(total(return_dict)/len(return_dict)))
			print("Number of completed requests: " + str(len(return_dict)))


		else:
			print("Total turn-around time: " + str(total(return_dict)))
			print("Average turn-around time: " + str(total(return_dict)/len(return_dict)))
			print("Number of completed requests: " + str(len(return_dict)))
			break



#message.encode(encoding='UTF-8')


