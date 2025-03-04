import os
import subprocess
import pytz
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    name = "Abhinav Anand"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
   
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
   
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -20", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"
   
    html = f"""
    <html>
    <head><title>/htop Output</title></head>
    <body>
        <h1>/htop Endpoint</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)