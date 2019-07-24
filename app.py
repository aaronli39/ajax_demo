from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ajax")
def handle():
    print("\n\n-------------------\nrunning server code\n---------------------\n")
    return {"output": str(len(request.args.get("input")))}

if __name__ == "__main__":
    app.debug = True
    app.run()