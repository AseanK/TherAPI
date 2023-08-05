from flask import Flask, render_template, request, jsonify
import openai
import config
import requests

openai.api_key = config.Config.OPENAI_KEY
app = Flask(__name__)
app.config["SECRET_KEY"] = config.Config.SECRET_KEY

# openAI messages
messages = [{"role": "system", "content": "You're a therapist, help user calm and relax. Be polite and if the user's content is irrelevant to mental health, let them know that your a therapist but still give them your answer. The website contains Beach, Forest, Fire, Rain, River, Snow, and Space theme. Suggest one of the theme that is rellavent to user's emotion."}]


# API call
def get_quote():
    category = 'inspirational'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    return requests.get(api_url, headers={'X-Api-Key': config.Config.API_KEY}).json()
    


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.form.get("message")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    result = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": result})
    print(messages)
    return jsonify({"response": result})


@app.route("/beach")
def beach():
    return render_template("beach.html")


@app.route("/forest")
def forest():
    return render_template("forest.html", quote=get_quote())


@app.route("/space")
def space():
    return render_template("space.html", quote=get_quote())


@app.route("/rainy")
def rainy():
    return render_template("rainy.html", quote=get_quote())


@app.route("/river")
def river():
    return render_template("river.html", quote=get_quote())


@app.route("/fire")
def fire():
    return render_template("fire.html", quote=get_quote())


@app.route("/snow")
def snow():
    return render_template("snow.html", quote=get_quote())



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