from tkinter import *
from time import sleep
import threading #import the library
import socketserver

class MyTCPHandler1(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.ip_address = self.client_address[0]
        self.data_decode = self.data.decode("utf-8")
        print(self.ip_address)
        #print(self.data_decode)
        
        if len(measurements_1_list) < 3:
            measurements_1_list.append(self.data_decode)
        print(measurements_1_list)

class MyTCPHandler2(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.ip_address = self.client_address[0]
        self.data_decode = self.data.decode("utf-8")
        print(self.ip_address)
        #print(self.data_decode)
        
        if len(measurements_2_list) < 3:
            measurements_2_list.append(self.data_decode)
        print(measurements_2_list)
            

class MyTCPHandler3(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.ip_address = self.client_address[0]
        self.data_decode = self.data.decode("utf-8")
        print(self.ip_address)
        #print(self.data_decode)
        
        if len(measurements_3_list) < 3:
            measurements_3_list.append(self.data_decode)
        print(measurements_3_list)


def reset_value_1():
    global measurements_1_list
    measurements_1_list = []

def reset_value_2():
    global measurements_2_list
    measurements_2_list = []

def reset_value_3():
    global measurements_3_list
    measurements_3_list = []

def tcp_server(port,mytcp):
    HOST = "localhost"
    server = socketserver.TCPServer((HOST, port), mytcp)
    server.serve_forever()      



def call():
    while True:
        if len(measurements_1_list)==0:
            l1.config(text="init")
            l2.config(text="init")
            l3.config(text="init")
        elif len(measurements_1_list)==1:
            l1.config(text=measurements_1_list[0])
            l2.config(text="init")
            l3.config(text="init")
        elif len(measurements_1_list)==2:
            l1.config(text=measurements_1_list[0])
            l2.config(text=measurements_1_list[1])
            l3.config(text="init")
        elif len(measurements_1_list)==3:
            l1.config(text=measurements_1_list[0])
            l2.config(text=measurements_1_list[1])
            l3.config(text=measurements_1_list[2])
        else:
            print('error')

        if len(measurements_2_list)==0:
            l4.config(text="init")
            l5.config(text="init")
            l6.config(text="init")
        elif len(measurements_2_list)==1:
            l4.config(text=measurements_2_list[0])
            l5.config(text="init")
            l6.config(text="init")
        elif len(measurements_2_list)==2:
            l4.config(text=measurements_2_list[0])
            l5.config(text=measurements_2_list[1])
            l6.config(text="init")
        elif len(measurements_2_list)==3:
            l4.config(text=measurements_2_list[0])
            l5.config(text=measurements_2_list[1])
            l6.config(text=measurements_2_list[2])
        else:
            print('error')

        if len(measurements_3_list)==0:
            l7.config(text="init")
            l8.config(text="init")
            l9.config(text="init")
        elif len(measurements_3_list)==1:
            l7.config(text=measurements_3_list[0])
            l8.config(text="init")
            l9.config(text="init")
        elif len(measurements_3_list)==2:
            l7.config(text=measurements_3_list[0])
            l8.config(text=measurements_3_list[1])
            l9.config(text="init")
        elif len(measurements_3_list)==3:
            l7.config(text=measurements_3_list[0])
            l8.config(text=measurements_3_list[1])
            l9.config(text=measurements_3_list[2])
        else:
            print('error')

        sleep(1)
            

root = Tk()
    # Set geometry
root.geometry("400x400")

measurements_1_list = []
measurements_2_list = []
measurements_3_list = []


l1 = Label(root) #empty label
l1.pack() #pack()
l2 = Label(root) #empty label
l2.pack() #pack()
l3 = Label(root) #empty label
l3.pack() #pack()
reset_1 = Button(root, text = "reset1",command = reset_value_1).pack()

l4 = Label(root) #empty label
l4.pack() #pack()
l5 = Label(root) #empty label
l5.pack() #pack()
l6 = Label(root) #empty label
l6.pack() #pack()
reset_2 = Button(root, text = "reset2",command = reset_value_2).pack()

l7 = Label(root) #empty label
l7.pack() #pack()
l8 = Label(root) #empty label
l8.pack() #pack()
l9 = Label(root) #empty label
l9.pack() #pack()
reset_3 = Button(root, text = "reset3",command = reset_value_3).pack()


t1 = threading.Thread(target=tcp_server, args=(9999,MyTCPHandler1))
t1.start()
t2 = threading.Thread(target=tcp_server, args=(9998,MyTCPHandler2))
t2.start()
t3 = threading.Thread(target=tcp_server, args=(9997,MyTCPHandler3))
t3.start()

threading.Thread(target=call).start()

root.mainloop()