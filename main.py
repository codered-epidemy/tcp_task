import socket
import threading
import time


list_of_ports = list()


def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        conn = s.connect((ip, port))
        list_of_ports.append(port)
        time.sleep(5)
        s.close()
    except:
        pass


try:
    addr = input("Enter IP or domain: ")
    address = socket.gethostbyname(addr)
except:
    raise IOError("Inputted value might be incorrect IP or domain")

print(socket.gethostbyname(address))
start_port, end_port = input("Enter start port and end port: ").split(" ")
for i in range(int(start_port), int(end_port) + 1):
    thread = threading.Thread(target=scan_port, args=(address, i))
    thread.start()

if len(list_of_ports) == 0:
    print("No open ports")
else:
    print("Open ports:", *list_of_ports)
