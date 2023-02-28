from flask import Flask, jsonify, request, redirect, render_template
from taal import doEncryption, undoEncryption

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Enter Text')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    notes = doEncryption(message=message.lower())
    return render_template(
                            'post.html', title='Encrypted Text', 
                            notes=notes.replace('_',' '),
                        )

@app.route('/decrypt', methods=['POST'])
def decrypt():
    notes = request.form['notes']
    text = "String too long" if notes=="String too long" else undoEncryption(notes=notes)
    return render_template(
                            'post.html', title='Decrypted Text', 
                            notes=text,
                        )

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='Error 404')

if __name__ == '__main__':
    app.run()