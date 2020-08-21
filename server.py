import socket
import sys

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

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if (len(str.encode(cmd)) > 0):
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()

main()