from flask import Flask, redirect, render_template, url_for, request
import openai
import config

openai.api_key = config.Config.OPENAI_KEY
app = Flask(__name__)
app.config["SECRET_KEY"] = config.Config.SECRET_KEY

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/beach")
def beach():
    return render_template("beach.html")


@app.route("/forest")
def forest():
    return render_template("forest.html")


@app.route("/space")
def space():
    return render_template("space.html")


@app.route("/rainy")
def rainy():
    return render_template("rainy.html")


@app.route("/river")
def river():
    return render_template("river.html")


@app.route("/fire")
def fire():
    return render_template("fire.html")


if __name__ == "__main__":
    app.run(debug=True)


# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message.content)