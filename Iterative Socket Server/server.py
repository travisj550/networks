import socket
import sys
import subprocess

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 3232 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
try:
    s.bind((HOST, PORT))
except (socket.error , msg):
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
s.listen(30)
print ('Socket now listening')
 
#now keep talking with the client
#wait to accept a connection - blocking call

#data = conn.recv(1024)

while 1:
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(1024)
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
            break
    except:
        print('Error')
        conn.close()
        s.close()
    date = result.stdout
    reply = 'CHOSEN' + data.decode()
    #print (reply)
    if not data: 
        break
    conn.sendall(date)
 
conn.close()
s.close()
