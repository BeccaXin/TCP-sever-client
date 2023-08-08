#python3
from socket import *
from threading import Thread
import sys, select
import datetime,time
import os

# acquire server host and port from command line parameter
if len(sys.argv) != 2:
    print("\n===== Error usage, python3 TCPServer3.py SERVER_PORT ======\n")
    exit(0)
serverHost = "127.0.0.1"
serverPort = int(sys.argv[1])
# serverPort=2096
serverAddress = (serverHost, serverPort)

# define socket for the server side and bind address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)



print("\n===== Server is running =====")
print("===== Waiting for connection request from clients...=====")


file_name="credentials.txt"
with open(file_name) as file:
    text=file.read()
    line=text.split("\n")
    line =[i for i in line if i != '']
    yonghuming=[]
    mima=[]

    for i in line:
        inf=i.split(" ")
        k=inf[0]
        kk=inf[1]
        yonghuming.append(k)
        mima.append(kk)

while True:
    serverSocket.listen()
    clientSockt, clientAddress = serverSocket.accept()

    tishidenglu = "Username:"
    clientSockt.send(tishidenglu.encode("utf-8"))
    #jieshouzhanghuming
    recvmsg = clientSockt.recv(1024)
    zhanghao = recvmsg.decode("utf-8")
    # print(zhanghao)
    duiying="no"
    yzjg="no"
    n=0
    for q in range(len(yonghuming)):
        if zhanghao in yonghuming:
            duiying=yonghuming.index(zhanghao)
            break

    tishidenglu_ = "Password:"
    clientSockt.send(tishidenglu_.encode("utf-8"))
    while True:
        recvmsg = clientSockt.recv(1024)
        keys = recvmsg.decode("utf-8")
        if duiying=="no":
            tishidenglu_shibai = "no"
            clientSockt.send(tishidenglu_shibai.encode("utf-8"))
        else:
            for iii in range(len(mima)):
                if keys==mima[duiying]:
                    yzjg="yes"

            if yzjg=="yes":
                file = open('userlog.txt', mode='a+')
                time1=time.strftime("%d %b %Y %H:%M:%S")
                active=f"{zhanghao} {time1}\n"
                file.write(active)
                file.close()
                tishidenglu_chenggong = "yes"
                #print("yes")
                clientSockt.send(tishidenglu_chenggong.encode("utf-8"))
                #传输第几个人
                time.sleep(0.1)
                file_ul = open('userlog.txt', mode='r')
                lines = len(file_ul.readlines())
                lines=str(lines)
                clientSockt.send(lines.encode("utf-8"))
                file_ul.close()
                break
                

            else:
                tishidenglu_shibai = "no"
                clientSockt.send(tishidenglu_shibai.encode("utf-8"))
    

    ID_exist=[]
    while True:
        recvmsg = clientSockt.recv(1024)
        functions = recvmsg.decode("utf-8")

        if functions=="ATU":
            aaa="ok"
            clientSockt.send(aaa.encode("utf-8"))#验证data_3
            atu=clientSockt.recv(1024)
            atu_1 = atu.decode("utf-8")
            print(f"{zhanghao} issued ATU command")
            with open('userlog.txt') as file2:
                text=file2.read()
                line=text.split("\n")
                line =[i for i in line if i != '']
                activeusers=[]
                file2.close()
                for i in line:
                    inf=i.split(" ")
                    activeusers.append(inf)
                #print(activeusers)
                d={}
                for iii in activeusers:
                    kkk=iii[0]
                    if kkk in d:
                        d[kkk] += 1
                    else:
                        d[kkk] = 1
                #出现次数，接下来删除本人的数据
                del d[atu_1]
                
                if len(d)!=0:
                    print("Return messages:")
#                    for keysss in d:
#                        if int(d[keysss])%2==0:
#                            del d[keysss]
                    active1=list(d)
                    n=0
                    for ii in active1:
                        for iii in activeusers:
                            yonghuming=iii[0]
                            shijian=iii[1]
                            shijian_1=iii[2]
                            shijian_2=iii[3]
                            shijian_3=iii[4]
                            
                            if ii==yonghuming:
                                print(f"{yonghuming}, active since {shijian} {shijian_1} {shijian_2} {shijian_3}.")
                                u=f"{yonghuming}, active since {shijian} {shijian_1} {shijian_2} {shijian_3}."
                                time.sleep(0.5)
                                clientSockt.send(u.encode("utf-8"))
                                # n+=1
                    # print(n)
                    time.sleep(0.5)
                    qqqq="wan"
                    time.sleep(0.5)
                    clientSockt.send(qqqq.encode("utf-8"))

                else:
                    qqqqq="no"
                    clientSockt.send(qqqqq.encode("utf-8"))

        elif "SRB" in functions:
            aa="ok"
            clientSockt.send(aa.encode("utf-8")) #验证data_3
            srb=clientSockt.recv(1024)
            srb_1 = srb.decode("utf-8")
            
            print(f"{zhanghao} issued SRB command")
            with open("userlog.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
                msg_srb=functions[4:]
                file4 = msg_srb.split(" ")
                jishu_1=0
                duoshaoren=len(file4)
                for i in file4:#pan duan cun zaima
                    for line in lines:
                        if i in line:
                            jishu_1+=1
                if jishu_1==duoshaoren:
                    print('Return message:')
                    fangjianhao=1
                    ID=1
                    while True:
                        filename_2=f"SR_{ID}_messagelog.txt"
                        if os.path.exists(filename_2) is True:
                            ID+=1
                            ID_exist.append(ID)
                        else:
                            ID_exist.append(ID)
                            break
                    file5 = open(f'SR_{ID}_messagelog.txt', mode='a+')
                    roomusers = zhanghao + ' ' + msg_srb
                    file5.writelines(roomusers+"\n")
                    file5.close()
                    aaaa=f"Separate chat room has been created, room ID:{ID}, users in this room:{zhanghao}, {msg_srb}"
                    print(aaaa)
                    clientSockt.send(aaaa.encode("utf-8"))
                else:
                    aaaaa="Some users are not active."
                    print(aaaaa)
                    clientSockt.send(aaaaa.encode("utf-8"))
    
        elif "SRM" in functions:
            mm="ok"
            clientSockt.send(mm.encode("utf-8"))
            if len(functions)>3:
                msg_srm=functions[4:]
                file6 = msg_srm.split(" ")
                # for i in file6:
                ID_srm_str=file6[0]
                ID_srm=int(file6[0])
                if ID_srm in ID_exist:
                    with open (f'SR_{ID_srm_str}_messagelog.txt',"r",encoding="utf-8") as f:
                        lines = f.readlines()
                        text=lines[0]
                        f.close()
#                            list_srm=[]
#                            for i in text:
#                                list_srm.append(i)
                        if zhanghao in text:
                            message_srm=functions[6:]
                            clientSockt.send(msg_srm.encode("utf-8"))
                            time4=time.strftime("%d %b %Y %H:%M:%S")
                            print(f"{zhanghao} issued a message in separate room {ID_srm_str}: #{ID_srm};{time4};{zhanghao};{message_srm}")
                            with open (f'SR_{ID_srm_str}_messagelog.txt',"a+",encoding="utf-8") as f1:
                                xieru=f"{time4};{zhanghao};{message_srm}"
                                f1.writelines(xieru+"\n")
                                f1.close()
                        else:
                            srm_reply_2='You are not in this separate room chat.'
                            print(srm_reply_2)
                            clientSockt.send(srm_reply_2.encode("utf-8"))
                else:
                    srm_reply_1="The separate room does not exist."
                    print(srm_reply_1)
                    clientSockt.send(srm_reply_1.encode("utf-8"))
                    break
                
        elif "RDM" in functions:
            rr="ok"
            clientSockt.send(rr.encode("utf-8"))
            k=functions[4]
            if k=="s":
                print(f"RDM command issued from {zhanghao}")
                # print("Return message")xiao
                RID=1
                q=functions[-8:-1]
                while True:
                    filename_3=f"SR_{RID}_messagelog.txt"
                    if os.path.exists(filename_3) is True:
                        # RID+=1
                        with open(filename_3,"r",encoding="utf-8") as f3:
                            liness = f3.readlines()[0]
                            text=liness
                            f3.close()

                        with open(filename_3,"r",encoding="utf-8") as f3:
                            suoyou = f3.readlines()[1:]
                            f3.close()
                        dijige=1
                        if zhanghao in text:
                            for i in suoyou:
                                sjxx=i
                                xiaoxi=i.split(" ")
                                shijian=i.split(";")
                                shijian_1=shijian[0]
                                xiaoxi_1=xiaoxi[3]
                                xiaoxi_2=xiaoxi_1.split(';')
                                xiaoxi_3=xiaoxi_2[0]
                                xiaoxi_31=xiaoxi_2[1]
                                xiaoxi_32=xiaoxi_2[2]
                                if q<xiaoxi_3:
                                    #chuanxiaoxi
                                    print("Return message")
                                    #room-1: #1; 1 Jun 2022 16:05:00; Yoda; hello there
                                    www=f'room-{RID}: #{dijige} {sjxx}'
                                    print(www)
                                    wwww=f'room-{RID}: #{dijige};{xiaoxi_31}:{xiaoxi_32} at {shijian_1}'
                                    dijige+=1
                                    clientSockt.send(wwww.encode("utf-8"))
                            RID+=1
                        else:
                            RID+=1
                    else:
                        if dijige==1:
                            print("no new message")
                            wwww_1="no"
                            clientSockt.send(wwww_1.encode("utf-8"))
                            break
                        else:
                            wwww_2="x"
                            clientSockt.send(wwww_2.encode("utf-8"))
                            break
            elif k=="b":
                print(f"RDM command issued from {zhanghao}")
                b=functions[-8:-1]
                with open('B_message.txt',"r",encoding="utf-8") as f4:
                    text_rdm=f4.read()
                    f4.close()
                xiaoxi_rdm=text_rdm.split("\n")
                xiaoxi_rdm.pop()
                j=1
                xiaoxi_r=1
                print("Return message")
                for g in xiaoxi_rdm:
                    rdm_b=g
                    xiaoxi_b=g.split(" ")
                    shijian_b=xiaoxi_b[8]
                    if b<shijian_b:
                        if xiaoxi_r==1:
                            print("Return message")
                        rrr=f"{rdm_b}"
                        print(rrr)
                        time.sleep(0.1)
                        clientSockt.send(rrr.encode("utf-8"))
                        j+=1
                        xiaoxi_r+=1
                if j==1:
                    c="No broadcast message"
                    print(c)
                    time.sleep(0.1)
                    clientSockt.send(c.encode("utf-8"))
                    break
                time.sleep(0.3)
                c_1="over"
                clientSockt.send(c_1.encode("utf-8"))
                    
            else:
                print("Error")
        
                pass
            
            
        elif functions=="OUT":
            print(f"{zhanghao} logout")
            clientSockt.send(functions.encode("utf-8"))
            qqq=zhanghao
            with open("userlog.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
                #print(lines)
            with open("userlog.txt","w",encoding="utf-8") as f_w:
                for line in lines:
                    if qqq in line:
                        continue
                    f_w.write(line)
            f.close()
            f_w.close()
            break
        elif "BCM" in functions:
            if len(functions)>3:
                msg1=functions[4:]
                clientSockt.send(msg1.encode("utf-8"))
                time2=time.strftime("%d %b %Y %H:%M:%S")
                print(f"{zhanghao} broadcasted BCM \"{msg1}\" at {time2}")
                file6 = open('B_message.txt', mode='a+')
                bcmusers = f"{zhanghao} broadcasted BCM \"{msg1}\" at {time2}"
                file6.writelines(bcmusers+"\n")
                file6.close()
            else:
                msg1="NO message"
                clientSockt.send(msg1.encode("utf-8"))
                #time2=time.strftime("%d %b %Y %H:%M:%S")
                print(f"{msg1}")
        else:
            
            aaa="Error. Invalid command!"
            clientSockt.send(aaa.encode("utf-8"))


    
