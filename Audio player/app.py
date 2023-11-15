from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)

@app.route('/templates/<path:filename>')
def serve_js(filename):
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run()
