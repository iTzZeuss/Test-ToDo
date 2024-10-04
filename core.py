from flask import Flask, render_template
import os 
import config

app = Flask(__name__)

@app.route('/')
def main_page():
    #FORFRONTEND: returning index for user
    return render_template("index.html")

if __name__ == '__main__':
    # Just running the app. nothing interesting in here. Mb we will need to setup ssl here
    port = int(os.environ.get('PORT', config.DEFAULT_PORT))
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)
