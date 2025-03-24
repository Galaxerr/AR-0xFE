import os
from flask import Flask, request, send_file, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images')
def serve_image():
    filename = request.args.get('filename')

    if not filename:
        abort(400, "Manca la scimmia")

    file_path = os.path.join('images/monkes/monkes/monkes/monkes/monkes/', filename)

    try:
        return send_file(file_path)
    except FileNotFoundError:
        abort(404, "Scimmia non trovata")
    except Exception as e:
        abort(500, str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
