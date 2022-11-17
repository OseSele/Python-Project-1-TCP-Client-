import socket

# ss stands for server socket which I made an object of adn called the socket family and socket type 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#stores host name  with a method that gets the adress of the host 

host = socket.gethostname()
port = 555

# binds the host and the port with the object that was made which is called serversocket
s.bind(('150.250.133.235', port))

#setting up a tcp listener 
s.listen(3)

#cs stands for clientsocket info accepted from the client 
while True:
    clientsocket, address = s.accept()
    # statment telling the server we got connection from server, converts adress to a string
    
    print(" received connection from: %s " % str(address))

    # variable with print statment about a suceesful connection 
    message = 'hello! , you have succesfully connected to the server' + "\r \n"

    clientsocket.send(message.encode("ascii"))
    #closes the socket
    clientsocket.close()
