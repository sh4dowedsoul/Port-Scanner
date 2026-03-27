import sys
import socket
from datetime import datetime

if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("enter target like: py port_scanner.py google.com")
    sys.exit()

print("scanning target:",target)
print("time:",datetime.now())

try:
    for port in range(1,500):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))

        if result==0:
            print("port",port,"is open")

        s.close()

except KeyboardInterrupt:
    print("stopped by user")
    sys.exit()

except:
    print("error")
    sys.exit()