# Importing required modules
import socket
import sys
import ipaddress

# Extracting host_ip and port_num
try:
    host_ip = str(sys.argv[1])
    try:
        port_num = int(sys.argv[2])
    except:                                       # Exit if port number is not entered
        print("Please enter Port Number!")  

except:                                           # Exit if host ip is not entered
    print("Please enter Host Ip!")


# Creating socket
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Name: ', host_ip, ', Port no: ', port_num)

try:
    sckt.connect((host_ip, port_num))                               # Connecting to server
    print("Connection to the server established...")
    while(True):
        expression = input('Enter the mathematical expression :')   # Take input from client
        sckt.send(expression.encode())                              # Send the expression to server
        print("Server returned answer : ", sckt.recv(1024).decode())# Receive result from server

    sckt.close() 				                                    # Close the socket when done

# Throw exception when ctrl + C is pressed
except KeyboardInterrupt:
    print("\nConnection terminated by client!")
# Throw exception when unable to  connect to server
except:
    print("\nConnection to the server failed!")