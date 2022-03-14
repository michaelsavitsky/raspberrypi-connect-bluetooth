import bluetooth

print("Searching for bluetooth devices")

device_name = "SRS-XB21"
device_addr = None

devices = bluetooth.discover_devices()

for addr in devices:
	if device_name == bluetooth.lookup_name(addr):
		device_addr = addr
		break

print(devices)
print(device_name)
print(device_addr)
