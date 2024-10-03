from flask import Flask, render_template
import os 
import config

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

if __name__ == '__main__':
    # Get the PORT environment variable from Render (default to 5000 if not set)
    port = int(os.environ.get('PORT', 4000))
    
    # Bind to '0.0.0.0' so the app is accessible externally, and use the port from Render
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)
