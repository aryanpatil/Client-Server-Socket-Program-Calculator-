# Importing required modules
import socket
import sys
import threading

# Extracting host_ip and port_num
try:
    host_ip = str(sys.argv[1])
    try:
        port_num = int(sys.argv[2])
    except:                                       # Exit if port number is not entered
        print("Please enter Port Number!")  

except:                                           # Exit if host ip is not entered
    print("Please enter Host Ip!")


print("Server is active...")

while True:
    # Creating socket
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding socket to the port
    sckt.bind((host_ip, port_num))

    # Waiting for client to connect
    sckt.listen()

    # Establish connection with client.
    connection, addr = sckt.accept()
    print('Got connection from', addr)

    # Close the new socket so that no other client interferes
    sckt.close()

    # Loop until interrupt is received
    while True:
        try:
            equation = connection.recv(1024).decode()               # Receive expression from client
            if equation == "exit":                                                          
                connection.send("Exit".encode())                     
                break
            else:
                print("Server received : ", equation)               
                result = eval(equation)                             # Evaluating the equation
                connection.send(str(result).encode())               # Sending answer to client
        
        # Throw exception when the client exits
        except (socket.error):      
            print("Client Exits...")
            break
        # Exception for divide by zero
        except (ZeroDivisionError):
            connection.send("Attempted division by 0!".encode())
        # Exception for invalid syntax
        except (SyntaxError):
            connection.send("Invalid syntax detected!".encode())

    # Close the connection
    connection.close()