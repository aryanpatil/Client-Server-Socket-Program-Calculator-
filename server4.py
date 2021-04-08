# Importing required modules
import socket
import sys
import select
import queue as Queue

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

# Creating socket
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Keep the socket in non-blocking mode
sckt.setblocking(False)

# Binding socket to the port
sckt.bind((host_ip, port_num))

# Waiting for client to connect
sckt.listen()

# Initializing inputs and outputs
ins = [sckt]
outs = []
msgs = {}

# Loop until input list is non-empty
while ins:
    # Select() function
    read_list, write_list, error_list = select.select(ins, outs, ins)

    for rl in read_list:
        if rl == sckt:
            # Establish connection with client.
            connection, addr = sckt.accept()
            print('Got connection from', addr)
            connection.setblocking(False)
            ins.append(connection)                                  # Append connection to input list
            msgs[connection] = Queue.Queue()
        else:
            equation = rl.recv(1024).decode()                       # Receive expression
            if equation:
                if equation == "exit":
                    rl.send("Exit".encode())
                    break
                else:
                    print("Server received : ", equation)
                    result = equation                               # Echo the same expression
                    msgs[rl].put(result)                            # Add the result to queue
                    if rl not in outs:
                        outs.append(rl)
            else:
                if rl in outs:
                    outs.remove(rl)
                ins.remove(rl)
                rl.close()

                del msgs[rl]
                
            
    for wl in write_list:
        try:
            next_msg = msgs[wl].get_nowait()
        except Queue.Empty:
            outs.remove(wl)
        else:
            wl.send(str(next_msg).encode())                         # Sending answer to client 

    for ex in error_list:
        ins.remove(ex)
        if ex in outs:
            outs.remove(ex)
        ex.close()

        del msgs[ex]
