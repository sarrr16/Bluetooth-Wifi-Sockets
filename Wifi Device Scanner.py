import socket

def scan_local_network(ip_prefix):
    open_ports = []
    
    start_port = 1
    end_port = 1024

    for port in range(start_port, end_port + 1):
        target_ip = f"{ip_prefix}.{port}"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust the timeout as needed
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            open_ports.append(port)
            print(f"Port {port} on {target_ip} is open.")

        sock.close()

    return open_ports

def main():
    ip_prefix = "192.168.1.4"
    open_ports = scan_local_network(ip_prefix)

    if not open_ports:
        print("No open ports found on the local network.")
    else:
        print("Open ports found on the local network:", open_ports)

if __name__ == "__main__":
    main()

