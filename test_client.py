from fastmcp import Client
import asyncio
from bus_mgmt_dolt_mcp_server.bus_mgmt_dolt_mcp_server import mcp

async def call_tool(name: str):
    client = Client(mcp)
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result[0].text)

async def test_write_query():
    client = Client(mcp)
    async with client:
        # Example: Create a test table
        create_table = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INT PRIMARY KEY,
            name VARCHAR(50)
        )
        """
        result = await client.call_tool("write_query", {"sql": create_table})
        print("Create table result:", result[0].text)
        
        # Example: Insert data
        insert_data = "INSERT INTO test_table (id, name) VALUES (1, 'Test Name')"
        result = await client.call_tool("write_query", {"sql": insert_data})
        print("Insert data result:", result[0].text)
        
        # Example: Query the data to verify
        select_data = "SELECT * FROM test_table"
        result = await client.call_tool("query_data", {"sql": select_data})
        print("Query result:\n", result[0].text)

def test_client():
    print("Testing client...")
    asyncio.run(call_tool("Tom"))
    asyncio.run(call_tool("Jill"))
    asyncio.run(test_write_query())

if __name__ == "__main__":
    test_client()
