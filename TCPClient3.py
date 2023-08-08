#python3
from socket import *
import sys
import datetime,time
import os

#Server would be running on the same host as Client
if len(sys.argv) != 3:
    print("\n===== Error usage, python3 TCPClient3.py SERVER_IP SERVER_PORT ======\n")
    exit(0)
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
serverAddress = (serverHost, serverPort)

# define a socket for the client side, it would be used to communicate with the server
clientSocket = socket(AF_INET, SOCK_STREAM)

# build connection with the server and send message to it
clientSocket.connect(serverAddress)
n=0
while True:
    data = clientSocket.recv(1024)
    receivedMessage = data.decode()
    message_ac=input("Username:")
    yonghuming=message_ac
    clientSocket.send(message_ac.encode()) #shuruyonghuming
    while True:
        data_1 = clientSocket.recv(1024)
        receivedMessage = data_1.decode()
        # print(data_1)
        if len(data_1)>0:
            break
    while True:
        message_key=input("Password:")
        clientSocket.send(message_key.encode())
        data_2 = clientSocket.recv(1024)
        receivedMessage = data_2.decode()

        if receivedMessage=="yes":
            time1=time.strftime("%d %b %Y %H:%M:%S")
            user_ = clientSocket.recv(1024)
            user_math = user_.decode()
            print(f"{user_math}; {time1}; {yonghuming};{serverHost};{serverPort}")
            print("Welcome to TOOM!")
            break
        else:
            n+=1
            if n==3:
                print("Invalid Password. Your account has been blocked. Please try again later")
                time.sleep(10)
                n=0
            else:
                print("Invalid Password. Please try again")

    while True:
        mseeage=" "
        message = input("Enter one of the following commands (BCM, ATU, SRB, SRM, RDM, OUT, UPD):\n")
        clientSocket.send(message.encode())
        data_3 = clientSocket.recv(1024)
        receivedMessage = data_3.decode()
        if receivedMessage=="Error. Invalid command!":
            continue
        if 'BCM' in message:
            time2=time.strftime("%d %b %Y %H:%M:%S")
            print(f"Broadcast message,broadcast at {time2}")
        if receivedMessage=='OUT':
            print(f"Bye,{yonghuming}")
            break
            
        if message=='ATU':
            u=message_ac
            clientSocket.send(u.encode())
#            print()
#            msg_atu = clientSocket.recv(1024)
#            meg_atu1 = msg_atu.decode()
            while True:
                msg_atu = clientSocket.recv(1024)
                time.sleep(1)
                meg_atu1 = msg_atu.decode()
                if meg_atu1=="no":
#                    print("1")
                    print("no other active user.")
                    break
                elif meg_atu1 in " wanbi ":
                    break
                else:
                    time.sleep(0.1)
                    print(meg_atu1,end="\n")

        if 'SRB' in message:
            d=message_ac
            clientSocket.send(d.encode())
            msg_srb = clientSocket.recv(1024)
            meg_srb1 = msg_srb.decode()
            print(meg_srb1)
        if 'SRM' in message:
            msg_srm = clientSocket.recv(1024)
            meg_srm1 = msg_srm.decode()
            print(meg_srm1)
            
        if 'RDM' in message:
            kkkkk=message[6:]
            nnn=1
            k=message[4]
            if k=="s":
                while True:
                    msg_rdm = clientSocket.recv(1024)
                    meg_rdm1 = msg_rdm.decode()
                    if meg_rdm1 in " nonono ":
                        print("no new message")
                        break
                    elif len(meg_rdm1)>=2:
                        if nnn==1:
                            print(f"Messages in separate rooms since {kkkkk}")
                        print(meg_rdm1)
                        nnn+=1
                    else:
                        break
            elif k=="b":
                while True:
                    msg_rdm = clientSocket.recv(1024)
                    meg_rdm1 = msg_rdm.decode()
                    
                    if meg_rdm1 in " over ":
                        print("")
                        break
                    elif meg_rdm1 in " No broadcast message ":
                        print(meg_rdm1)
                        break
                    else:
                        print(meg_rdm1)
            else:
                print("Error")
                break
            
    break
clientSocket.close()
