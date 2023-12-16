import bluetooth
import socket

def discover_bluetooth_devices():
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, device_id=-1)

    if not devices:
        print("No nearby Bluetooth devices found.")
        return []

    for i in range(len(devices)):
        print(i, ":", devices[i])

    device_index = int(input("Which Device Is To Be Connected? "))

    if device_index < 0 or device_index >= len(devices):
        print("Invalid device index")
        exit(1)

    return devices[device_index]


if __name__ == "__main__":
    device = discover_bluetooth_devices()

    device_name = device[1]
    device_address = device[0]

    print(f"Device name: {device_name}")
    print(f"Device address: {device_address}")

    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    s.connect((device_address, 9))

    data = s.recv(1024)
    print(data)

    s.close()

    services = bluetooth.find_service(address=device_address)

    if len(services) <=0:

        print("zero services found on", device_address)