#configure networks
Make or find a wifi network that you know the password to a mobile hotspot works great for this.
###Put in ap mode
Connect to the drones wifi and use packet sender (https://packetsender.com/download#show) to send command "ap “wifi name” “wifi password”" to address 192.168.10.1 port 8889 it should say “OK,drone will reboot in 3s”
Repeat with all drones 
#connect to tellos
Connect computer to the same wifi network as the drones 
Use ip.py to find what is on in that network
Send “command” each ip that is online and if it is a tello it will reply “ok”
Send “sn?” to figure out what tello got which ip
#edit and run commands
Edit telloswarmcontroller.py to connect to the tellos and send the commands you want
Use the offical tello doc (https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) to see available commands.
