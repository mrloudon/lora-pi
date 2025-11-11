import asyncio

class UDPListenerProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        print(f"Received from {addr}: {data}")
    
    def error_received(self, exc):
        print(f"Error received: {exc}")


async def main():
    loop = asyncio.get_running_loop()
    transport, _ = await loop.create_datagram_endpoint(
        lambda: UDPListenerProtocol(),
        local_addr=('0.0.0.0', 5005)
    )
    print("Listening for UDP broadcasts on port 5005...")
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Listener stopped.")
    finally:
        transport.close()

# Use this in environments where asyncio.run() is restricted
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())

asyncio.run(main())