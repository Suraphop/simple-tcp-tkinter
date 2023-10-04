import socketserver
import time
import threading
from tkinter import *

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


def tcp_server(port,mytcp):
    HOST = "localhost"
    server = socketserver.TCPServer((HOST, port), mytcp)
    server.serve_forever()

def value():
    global measurements_1_list,measurements_2_list,measurements_3_list
    while True:
        print(measurements_1_list)
        print(measurements_2_list)
        print(measurements_3_list)
        time.sleep(5)

def reset_value():
    global measurements_1_list
    measurements_1_list = []

def show_data():
    global measurements_1_list
    var = StringVar()


    if len(measurements_1_list) > 0:
        var.set(measurements_1_list[0])
    else:
        var.set('init')
    text_show.config(text=var)

    root.after(1000,show_data)

if __name__ == "__main__":
        # Create Object
    root = Tk()
    
    # Set geometry
    root.geometry("400x400")

    measurements_1_list = []
    measurements_2_list = []
    measurements_3_list = []
    t1 = threading.Thread(target=tcp_server, args=(9999,MyTCPHandler1))
    t1.start()
    t2 = threading.Thread(target=tcp_server, args=(9998,MyTCPHandler2))
    t2.start()
    t3 = threading.Thread(target=tcp_server, args=(9997,MyTCPHandler3))
    t3.start()
    t4 = threading.Thread(target=value)
    t4.start()

    text_show = Label(root).pack()
    test = Button(root, text = "reset",command = reset_value).pack()

    root.after_idle(show_data)
    root.mainloop()