import bluetooth
import subprocess

device_addr = None
device_name = "SRS-XB21"
passkey = "0000"
port = 1
print("Searching for", device_name)

devices = bluetooth.discover_devices(duration=3, lookup_names=True)

for addr,name in devices:
	if device_name == name:
		device_addr = addr
		break

if device_addr is not None:
	print("Device found. Address:", device_addr)
else:
	print("Device not found")

# I found this part on StackOverflow, because of course I did
# subprocess.call("kill -9 `pidof bluetooth-agent`", shell=True)
# status = subprocess.call("bluetooth-agent " + passkey + " &", shell=True)

try:
	socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	socket.connect((device_addr, port))
except bluetooth.BluetoothError as err:
	print("Something went wrong idk")
	socket.close()
	pass

socket.recv(1024)
socket.send("What do I even put here")

socket.close()
