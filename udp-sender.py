import socket

def broadcast_udp(data: bytes, port: int = 5005):
    """
    Broadcast a short byte array using UDP.

    Args:
        data (bytes): Byte array to broadcast (must be <= 64 bytes).
        port (int): UDP port to broadcast on (default is 5005).
    """
    if not isinstance(data, bytes):
        raise TypeError("Data must be of type 'bytes'.")
    if len(data) > 64:
        raise ValueError("Data must be 64 bytes or less.")

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # socket option level = SOCKET, socket option name = BROADCAST, value = 1
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Broadcast to the local network
    broadcast_address = ('255.255.255.255', port)
    sock.sendto(data, broadcast_address)

    sock.close()

broadcast_udp(b'Hello, network!', port=5005)