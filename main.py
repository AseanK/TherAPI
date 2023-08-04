from flask import Flask, redirect, render_template, url_for, request
import openai
import config

openai.api_key = config.Config.OPENAI_KEY
app = Flask(__name__)
app.config["SECRET_KEY"] = config.Config.SECRET_KEY


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)