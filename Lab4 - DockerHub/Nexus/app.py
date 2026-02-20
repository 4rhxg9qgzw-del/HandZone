from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Python App inside Docker! 🐍</h1><p>Hello Daniel, the app is running smoothly.</p>'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)
