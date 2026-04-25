from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://test-remote-mcp-server-k1xt.onrender.com/mcp",
    name="Expense Proxy"
)

if __name__ == "__main__":
    mcp.run()