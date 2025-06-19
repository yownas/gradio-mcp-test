import gradio as gr
import time

url = ""

def cat_image() -> str:
    """
    Retrieve an image of a cat.

    Returns:
        A cat image.
    """
    result = {
        "path": "cat.png",
        "meta": {"_type": "gradio.FileData"}
    }
    print(f"Return image of a cat.")
    return result

def cat_url() -> str:
    """
    Retrieve a url to an image of a cat.
    Continue by formatting the url with markdown like this "![title](url)" to display it to the user.

    Returns:
        url (str): The url of the image.
    """
    result = url + "gradio_api/file/cat.png"
    print(f"Return: {result}")
    return result

with gr.Blocks() as demo:
    gr.Markdown(
        """
        This is a demo of a MCP-only tool.
        This tool slices a list.
        This tool is MCP-only, so it does not have a UI.
        """
    )
    gr.api(cat_image)
    gr.api(cat_url)

_, url, _ = demo.launch(
    mcp_server=True,
    allowed_paths=["."],
    prevent_thread_lock=True,
)

while True:
    time.sleep(100)
