import websockets
import asyncio

PORT = 7000
URL = 'localhost'
connections={}
next_name=[1] #mora da bude mutable, ne moze da bude int
async def glavna(ws, path):
    print("Klijent se zakacio")
    connections[ws]=next_name[0]
    next_name[0]+=1
    await ws.send("Prikljucio si se")
    try:
        async for poruka in ws:
            print("Poruka: " + poruka)
            for otherws in connections.keys():
                if not ws == otherws:
                    await otherws.send(str(connections[otherws])+" kaze " + poruka)
            
    except websockets.exceptions.ConnectionClosedError:
        print("Klijent se neocekivano otkacio")
    finally:    
        connections.pop(ws)


async def serve():
    
    wsserver = websockets.serve(glavna, URL, PORT)
    async with wsserver:
        await asyncio.Future()

asyncio.run(serve())
#serve vraca klasu websocketserver
#to ima interface kao asyncio server
# asyncio.get_event_loop().run_until_complete(wsserver)
# asyncio.get_event_loop().run_forever()