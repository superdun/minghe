from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/gzhindex")
def gzhIndex():
    items = range(12)
    return render_template("gzhIndex.html",items=items)
if __name__ == '__main__':
    app.run()
