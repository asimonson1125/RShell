import socket
import sys
import time

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9985
        s = socket.socket()
    except socket.error as msg:
        print("socket creation failure: " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding to port " + str(port))
        s.bind((host, port))
        s.listen(3)
    except socket.error as msg:
        print("socket bind failure: " + str(msg))
        bind_socket()

def accept_socket():
    conn, address = s.accept()
    print("Connection established, IP: " + address[0] + " Port: " +str(address[1]))
    send_commands(conn)
    conn.close()

End='>!!> '
def recv_end(conn):
    total_data=[];data=''
    while True:
            data=str(conn.recv(1024), "utf-8")
            if data[len(data) - len(End):] == End:
                total_data.append(data)
                break
            total_data.append(data)
            if len(total_data)>1:
                # check if end_of_data was split
                last_pair=total_data[-2]+total_data[-1]
                if End in last_pair:
                    total_data[-2]=last_pair[:last_pair.find(End)]
                    total_data.pop()
                    break
    return ''.join(total_data)

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if (len(str.encode(cmd)) > 0):
            conn.send(str.encode(cmd))
            print(recv_end(conn[0]), end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()

main()