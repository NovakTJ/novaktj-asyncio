import websockets
import asyncio

PORT = 7000

svi = set()

async def glavna(ws, path):
    print("Klijent se zakacio")
    await ws.send("Prikljucio si se")
    svi.add(ws)
    try:
        async for poruka in ws:
            print("Poruka: " + poruka)
            websockets.broadcast(svi, "Neko kaze " + poruka)
    except websockets.exceptions.ConnectionClosedError:
        print("Klijent se neocekivano otkacio")
    finally:    
        svi.remove(ws)

wsserver = websockets.serve(glavna, "localhost", PORT)
#serve vraca klasu websocketserver
#to ima interface kao asyncio server
asyncio.get_event_loop().run_until_complete(wsserver)
asyncio.get_event_loop().run_forever()