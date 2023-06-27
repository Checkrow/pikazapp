from flask import Flask, jsonify,send_file
import os
app=Flask(__name__)
@app.route('/')
def hello_world():
    return send_file("static/index.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
