# Configure Networks
Make or find a wifi network that you know the password to a mobile hotspot works great for this.

## Put in "ap" Mode
1. Connect to the drones wifi and use [Packet Sender](https://packetsender.com/download#show) to send command `ap “wifi name” “wifi password”` to address 192.168.10.1 port 8889 it should say “OK,drone will reboot in 3s”
2. Repeat with all drones 

## Connect to Tellos
1. Connect computer to the same wifi network as the drones 
2. Use ip.py to find what is on in that network
3. Send `command` each ip that is online and if it is a tello it will reply “ok”
4. Send `sn?` to figure out what tello got which ip

# Edit and Run Commands
1. Edit telloswarmcontroller.py to connect to the tellos and send the commands you want
2. Use the [offical tello doc](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) to see available commands.
