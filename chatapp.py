import os
from flask import Flask, redirect, render_template, request


app = Flask(__name__)
messages = []
naughty_words=["cat","dog", "trump", "luca"]

@app.route("/")
def get_index():
    return render_template("index.html")
    
@app.route("/login")
def do_login():
    username = request.args['username']
    return redirect(username)
    
@app.route("/<username>")
def get_userpage(username):
    return render_template("chat.html", username=username, messages=messages)
    
@app.route("/<username>/new", methods=["POST"])
def add_message(username):
    text = request.form['message']
    
    words = text.split()
    for i in range(len(words)):
        if words[i].lower() in naughty_words:
            words[i] = "*" * len(words[i])
    
    text = " ".join(map(str, words))
    
    
    
    message = {
        'sender': username,
        'body': text
    }
    messages.append(message)
    return redirect(username)

    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))