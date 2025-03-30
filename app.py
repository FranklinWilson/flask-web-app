from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/users/')
def users(user_list=None):
    user_list = ['user 1', 'user 2', 'user 3']
    return render_template('list.html', users=user_list)

if __name__ == "__main__":
    app.run(debug=True)
