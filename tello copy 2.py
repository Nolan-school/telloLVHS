# This example script demonstrates how to use Python to fly Tello in a box mission
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello

tello1ip = input("Enter Tello 1 ip ")


tello1_address = (tello1ip, 8889)

tello2ip =input( "Enter Tello 2 ip ")

tello2_address = (tello2ip, 8889)



# IP and port of local computer
local1_address = ('', 9010)
local2_address = ('', 9011)

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock1.bind(local1_address)
sock2.bind(local2_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay, sn):
  # Try to send the message otherwise print the exception
  if sn == 1:
    try:
      sock1.sendto(message.encode(), tello1_address)
      print("Sending message: " + message)

    except Exception as e:
      print("Error sending: " + str(e))

      
  elif sn == 2:
      try:
        sock2.sendto(message.encode(), tello2_address)
        print("Sending message: " + message)
      except Exception as e:
        print("Error sending: " + str(e))

  else:

      try:
        sock1.sendto(message.encode(), tello1_address)
        sock2.sendto(message.encode(), tello2_address)
        print("Sending message: " + message)
      except Exception as e:
        print("Error sending: " + str(e))
  

  # Delay for a user-defined period of time
#time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock1.close()
      sock2.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()





#----------------------------------------------- edit between dashed lines with the tello sdk docs----------------------------------------

#use format send("command from the docs", delay in secs , tello number (0  for both)


# Put Tellos into command mode
send("command", 3, 0)

# Takeoff #1 and wait 3 sec
send("takeoff", 3 , 1)

# Takeoff #2 and wait 3 sec
send("takeoff", 3 , 2)


# Land both
send("land", 5 , 0)

# Print message
print("Mission completed successfully!")




#----------------------------------------------- edit between dashed lines with the tello sdk docs----------------------------------------



# Close the socket
sock1.close()
sock2.close()
