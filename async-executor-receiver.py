import asyncio
import socket

async def udp_listener(port):
    # Create the UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))

    print(f"Listening for UDP packets on port {port}...")

    while True:
        # Wait for a packet
        data, addr = await asyncio.get_event_loop().run_in_executor(None, sock.recvfrom, 1024)

        # Process the received data
        print(f"Received message from {addr}: {data.decode()}")

# To run the listener
async def main():
    port = 5005  # Specify the port to listen on
    await udp_listener(port)

# Start the asyncio event loop
asyncio.run(main())
