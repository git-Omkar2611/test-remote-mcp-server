from fastmcp import FastMCP
import random
import json


mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args 
    a : first number
    b : second mumber
    """
    return a + b

@mcp.tool
def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract two numbers together.
    
    Args 
    a : first number
    b : second mumber
    """
    return a - b

#Resource : Server info
@mcp.resource("info://server")
def server_info() -> str :
    """
    Get Information about this server
    """
    info = {
        "name" : "Simple Calculator Service" ,
        "version" : "1.0.0" ,
        "description" : "A basic MCP sv with math tools" ,
        "tools" : ["add_numbers" , "subtract_numbers"] ,
        "author" : "Omkar"
    }
    
    return json.dumps(info , indent = 2)


if __name__ == "__main__":
    mcp.run(transport="streamable-http" , host="0.0.0.0" , port = 8000)
