# Client-Server-Socket-Program-Calculator
The client chats with a custom 'Calculator' server. Expression is sent to the server via connected socket and the server computes the result and sends back to the client.

1. `client.py` : A client program which establishes socket connection with the server and communicates 
with the server for information exchange.

1. `server1.py` : A single process server that can
handle only one client at a time. If a second client tries to chat with the server while some
other client's session is already in progress, the second client's socket operations should
see an error. After the first client closes the connection, the server then accepts
connection from the other client.

2. `server2.py` : A multi-threaded server that will
create a new thread for every new client request it receives. Multiple clients are
able to simultaneously chat with the server.

3. `server3.py` : A single process server that uses
the "select" method to handle multiple clients concurrently.

4. `server4.py` : An echo server (that replies the
same message to the client that was received from the same client). It is a single
process server that uses the "select" method to handle multiple clients concurrently.

# How to Run ? 

1. Start the required server in the terminal using following commmand:<br />
`python server<number>.py <ip address> <port number>` <br />
Example : *python server1.py 192.167.2.9 5050*

2. In another terminal, start as many clients as required using following command:<br />
`python client.py <ip address> <port number>` <br />
Example : *python client.py 192.167.2.9 5050*
