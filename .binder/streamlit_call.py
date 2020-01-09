from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('simple-streamlit-app')
    Popen(["streamlit", "run", "app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
