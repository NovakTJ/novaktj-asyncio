import websockets
import asyncio
import aioconsole

url = "ws://localhost:7000"

otkaci = False
async def rukovanje():
    ws = await websockets.connect(url)
    await ws.send('Cao')
    return ws
    
async def primi(ws):
    async for poruka in ws: #zauvek se proverava
        print(poruka)

async def salji(ws):
    while True:
        str = await aioconsole.ainput()
        if str=="kraj" :
            await ws.send("Dovidjenja")
            await ws.close()
            print("Otkacio sam se")
            break
        else: await ws.send(str)

async def glavna():
    try:
        ws = await rukovanje()
        await asyncio.gather(salji(ws), primi(ws))
        #konkurentan rad
    except websockets.exceptions.ConnectionClosed:
        print("Konekcija je zavrsena")

asyncio.run(glavna())