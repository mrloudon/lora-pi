import uasyncio as asyncio
import socket

# Configure UDP listener
UDP_PORT = 12345

# Function to create a UDP listener
def create_udp_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', UDP_PORT))
    return sock

# Polling coroutine to check for incoming packets
async def poll_udp(sock):
    while True:
        # Set a timeout for non-blocking behavior
        sock.setblocking(False)
        try:
            data, addr = sock.recvfrom(1024)  # Non-blocking receive
            print(f"Received message from {addr}: {data.decode()}")
        except BlockingIOError:
            # If no data is available, just ignore and continue polling
            pass
        
        await asyncio.sleep(1)  # Sleep for 1 second before checking again

async def main():
    udp_sock = create_udp_socket()
    await poll_udp(udp_sock)

# Start the asyncio event loop
asyncio.run(main())
