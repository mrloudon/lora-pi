import socket

def listen_udp_broadcast(port: int = 5005, buffer_size: int = 1024):
    """
    Listen for UDP broadcast messages on the specified port.

    Args:
        port (int): Port to listen on.
        buffer_size (int): Size of the receive buffer.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))  # Bind to all interfaces

    print(f"Listening for UDP broadcasts on port {port}...")
    try:
        while True:
            data, addr = sock.recvfrom(buffer_size)
            print(f"Received from {addr}: {data}")
    except KeyboardInterrupt:
        print("Listener stopped.")
    finally:
        sock.close()

listen_udp_broadcast(port=5005)