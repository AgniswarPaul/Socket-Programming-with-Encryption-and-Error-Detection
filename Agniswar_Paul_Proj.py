##############################################################################################
# This program is for the client side to implement socket programming.
# At first, the client sends an introductory message to the server 
# to start the communication. The server then sends mathematical
# expressions to the client. Client evaluates the expression and sends
# back the result to the server. If the evaluation is wrong then the 
# server sends a failure message to the client indiacting that the last
# evaluation was wrong. If all the evaluations are correct then server
# sends a success message to the client which contains a secret FLAG.

# This program is created by Agniswar Paul.

# NU ID: 002112950

# FLAG that is received is:  ac29e7983dfb8f5d88aa81a809226692bd1b77a11209e0559dd4bc1613743e75

##############################################################################################

import socket # importing libary required to implement socket programming

# Details of the server----------------------------------------------------------------------
serverName = 'kopi.ece.neu.edu' # name of the server
serverPort = 5207 # port number to listen and establish the connection

# Socket Creation----------------------------------------------------------------------------
clientTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.socket() creates the socket
# socket.AF_INET indicates the internet address family (IPv4)
# socket.SOCK_STREAM indicates the socket type of TCP
# TCP connection will be used here to implement socket programming 


clientTCP.connect((serverName, serverPort))
# Client connects to the server using the server details mentioned above

msg1="EECE7374 INTR 002112950"  # Introductory message of client that contains NU ID

clientTCP.send(msg1.encode('utf-8'))
# Client sends the introductory message to the server by encoding using 
# UTF-8 unicode standard.


# Mathematical Expression Evaluation --------------------------------------------------------

while True: # using while loop to evaluate the expressions till success message is receive

    modified_msg1=clientTCP.recv(1024) # client receive the modified message from server

    print(modified_msg1.decode('utf-8')) # prints the modified message by decoding 

    list = modified_msg1.decode('utf-8').split() 
    # a 'list' variable is declared to store the modified message.
    # split() function is used to convert the message which is in string data type to 
    # list data type.

    text=list[1] # variable 'text' to store 1st index element of list

    if text=='SUCC': 
        break # breaking the while loop when the success message is receive

    else:  # continue to evaluate the expressions

        first_number=int(list[2]) 
        # variable 'first number' to store 2nd index element of list in integer data type

        operator=list[3] # variable 'operator' to store 3rd index element of list 

        second_number=int(list[4]) 
        # variable 'second number' to store 4th index element of list in integer data type

        # Expression evaluation technique -------------------------------------------------------
        if operator=='+':
                answer=first_number+second_number
        elif operator=='-':
                answer=first_number-second_number
        elif operator=='*':
                answer=first_number*second_number
        elif operator=='/':
                answer=first_number/second_number
        #----------------------------------------------------------------------------------------
        
        result=str(answer) # variable 'result' to store the evaluation result in string data type  

        msg2="EECE7374 RSLT " + result 
        # variable 'msg2' to store the result in a format according the assignment requirement 
        # before sending the result to the server.  

        clientTCP.send(msg2.encode('utf-8'))
        # client sends 'msg2' which contains the result to the server and the whole process repeats
        # till success message is receive that contains the secret flag. 


#----------------------------------- End of the Program -------------------------------------------

    









