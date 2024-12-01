from flask import Flask, send_file,render_template
app = Flask(__name__)



@app.route('/audio')
def send_audio():
    return send_file('recorded_audio.wav', as_attachment=True)

@app.route('/text')
def send_text():
    pass

if __name__ == '__main__':
    app.run(debug=True)
