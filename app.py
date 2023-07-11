from flask import Flask

app = Flask (__name__)
@app.route('/')
def index():
    return "Hola no sé cómo le hice"
app.run(host= '0.0.0.0', port=8888)