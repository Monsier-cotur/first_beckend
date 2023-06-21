from flask import Flask, render_template
app = Flask(__name__)

@app.route("/a")
def index():
    user={
        "name":"alua",
        "age":14
    }
    return render_template("index.html",  user=user)
@app.route("/")
def profile():
    ert={
        "name": "алуа",
        "age": 14,
        "hobby": "спать"
    }
    return render_template("profile.html", ert=ert)
if __name__ == "__main__":
    app.run(debug=True)