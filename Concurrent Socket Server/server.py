import socket
import sys
import subprocess
import time
from multiprocessing import *

def threaded(conn):

    print(time.time())
    data = conn.recv(1024)

    if not data:
        return

    try:
        if(data.decode() == '1'):
            result = subprocess.run(['date'], stdout=subprocess.PIPE)
        elif(data.decode() == '2'):
            result = subprocess.run(['uptime'], stdout=subprocess.PIPE)
        elif(data.decode() == '3'):
            result = subprocess.run(['free','-m'], stdout=subprocess.PIPE)
        elif(data.decode() == '4'):
            result = subprocess.run(['netstat'], stdout=subprocess.PIPE)
        elif(data.decode() == '5'):
            result = subprocess.run(['w'], stdout=subprocess.PIPE)
        elif(data.decode() == '6'):
            result = subprocess.run(['ps'], stdout=subprocess.PIPE)
        else:
            return
    except:
        print('Error')
        conn.close()
        #s.close()
    
    date = result.stdout
    reply = 'CHOSEN' + data.decode()
    #print (reply)
    conn.sendall(date)

    conn.close()
    
def Main():

    HOST = ''   # Symbolic name meaning all available interfaces
    PORT = 7783 # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Socket created')
    try:
        s.bind((HOST, PORT))
    except (socket.error , msg):
        print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print ('Socket bind complete')

    s.listen(120)

    print ('Socket now listening')

    processes = []

    #start = time.time()
    #print (start)
    #current = 0
    while(True):

        # establish connection with client
        conn, addr = s.accept()

        #start_new_thread(threaded ,(conn,))

        t = Process(target=threaded, args=(conn,))
        t.start()
        #t.join()
        #processes.append(t)
        #current = time.time()
        #print (current)
                    
        #for t in processes:
            #t.start()
        #for t in processes:
            #t.join()
    
    s.close()

if __name__ == '__main__':
    Main()
