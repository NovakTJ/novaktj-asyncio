import websockets
import asyncio

PORT = 7000
URL = 'localhost'
connections={}
next_name=1
async def glavna(ws, path):
    print("Klijent se zakacio")
    global next_name
    connections[ws]=next_name
    await ws.send("Prikljucio si se. Tvoj ID je " + str(next_name))
    next_name+=1
    try:
        async for poruka in ws: #zauvek se proverava
            print("Poruka: " + poruka)
            for otherws in connections.keys():
                if not ws == otherws:
                    await otherws.send(str(connections[ws])+" kaze " + poruka)
            
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