from flask import Flask, render_template
import requests
app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=data)


@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", post=data[num - 1])


if __name__ == "__main__":
    app.run(debug=True)
