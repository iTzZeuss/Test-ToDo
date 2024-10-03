from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Hello Render! I am UAGoose writing from backend"

if __name__ == '__main__':
    app.run(debug=config.DEBUG)
