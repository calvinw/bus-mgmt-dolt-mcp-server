from fastmcp import Client
import asyncio
from bus_mgmt_dolt_mcp_server.bus_mgmt_dolt_mcp_server import mcp

async def call_tool(name: str):
    client = Client(mcp)
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result[0].text)

def test_client():
    print("Testing client...")
    asyncio.run(call_tool("Tom"))
    asyncio.run(call_tool("Jill"))

if __name__ == "__main__":
    test_client()
