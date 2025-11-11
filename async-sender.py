import asyncio
import socket

async def broadcast_udp(data: bytes, port: int = 5005):
    if not isinstance(data, bytes):
        raise TypeError("Data must be of type 'bytes'.")
    if len(data) > 64:
        raise ValueError("Data must be 64 bytes or less.")

    await asyncio.sleep(1)  # Optional delay
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_address = ('255.255.255.255', port)
    sock.sendto(data, broadcast_address)
    sock.close()
    print("Broadcast sent.")

async def main():
    print("Sending...")
    await broadcast_udp(b'Hello, network 1!', port=5005)
    await asyncio.sleep(1)
    await broadcast_udp(b'Hello, network 2!', port=5005)
    print("Done!")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

asyncio.run(main())