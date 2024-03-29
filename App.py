from flask import Flask

app = Flask(__name__)

if(__name__=='main'):
    app.run(port=3000, debug=True)
