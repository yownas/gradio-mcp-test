Setup:

* Create a virtualenv with `python -m venv venv`
* Activate it `source venv/bin/activate`
* Install requirements `pip install -r requirements`
* Run the server `python app.py`

Edit MCP.json:
```
{
  "mcpServers": {
    "gradio-mcp-test": {
      "url": "http://localhost:7860/gradio_api/mcp/sse"
    }
  }
}
```

The server has two tools. `cat_image` which will return a PNG image of a cat and `cat_url` that only return the url and ask the LLM to display it using Markdown.
