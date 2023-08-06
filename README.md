## 💡 Inspiration
A study conducted by [the American Institute of Stress](https://www.stress.org/stress-level-of-americans-is-rising-rapidly-in-2022-new-study-finds) in April 2022 shows the stress level of Americans is rising rapidly. Most of us don't realize how the stressful environment surrounds us every day in life, and 
to make it worse, we may not know how to deal with stress. [TherAPI](https://ther-api-c28b9e2ec410.herokuapp.com) is the solution to this problem.

## 🔍 What it does
TherAPI is a website that aims to help anyone who seeks to reduce their stress level, take a break, seek professional advice, share their thoughts, or even focus on their work. 
TherAPI has three main components that users can interact with:
- An AI therapist chatbot that is customized for the website.
- Various nature-themed platforms where users can immerse themselves in serene natural landscapes.
- Random inspirational quotes to further enhance their mental well-being.

### AI therapist chatbot
The AI therapist chatbot is designed and customized to provide trustworthy guidance and a calming presence. 
The virtual therapist will also suggest one of the themes that best suits the user. 
If the user provides a question that is irrelevant to mental health, the chatbot will state that the question is irrelevant but still provide an answer in a mannerly way.

### Nature-themed platform
Each theme is accompanied by a corresponding nature picture and soothing sounds, such as the gentle lapping of waves at the beach or the rustling of leaves in a forest. 
According to the following studies:
- Gösta Ekman Laboratory, Department of Psychology, Stockholm University (February 2010)
  - [Stress Recovery during Exposure to Nature Sound and Environmental Noise](https://www.mdpi.com/1660-4601/7/3/1036)
- The Pennsylvania State University Department of Recreation, Park and Tourism Management (August 2015)
  - [THE INFLUENCE OF NATURAL SOUNDS ON ATTENTION RESTORATION](https://d1wqtxts1xzle7.cloudfront.net/78029856/4bc5f8ed3ce4c3355bb1af4bf556797ad22d-libre.pdf?1641312726=&response-content-disposition=inline%3B+filename%3DThe_Influence_of_Natural_Sounds_on_Atten.pdf&Expires=1691210850&Signature=LSmYPxxxx72CMQp8elsINIX5XqBJjmGGY~9BwkPX01rJT0obhLspnhKT18uSrt9nXThZwaijDnYLQTJQkTlxU62mbIaq1TfX9PeoG~JmRQgIQfx-YApw1gjLeqXj1t9FGfrcNG20VYFYx9I9ED4kVeOdLXpg3oZ07uLYTUvuQiSAo2hDbTKSnGEYloEjzNExlqg-rhLgc09RO2XldvKyGy2vVr-MtVLEvBeI~-1-2CE3gofyzK4wGgNlAfn76tvGFP3D8iF2SPmOPW1Y54BxfNXNr4iv55vzHVLsAvv0fLBQGuJ~eB5eYPwwOguOd0MTihSzQlFkc~TB4LGvXTlnEw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

The physiological recovery of sympathetic activation was up to 37% faster during exposure to pleasant nature sounds. 
Participants who listened to natural sounds mentally recovered from the initial depletion task significantly outperformed those who listened to no sound.
There are numerous studies that prove how the sounds of nature can affect one's mental health. 
I strongly recommend you check out some of the works. I find it quite interesting.

### Inspirational quotes
"Success is not final; failure is not fatal: It is the courage to continue that counts." — Winston S. Churchill. 
This is the quote that I have on my desk. I personally find a lot of impact in reading inspirational quotes. Along with the nature-themed page, a random inspirational quote is displayed on the page.

## 👨‍💻 How we built it
TherAPI is mainly built with Python, JavaScript, HTML, and CSS with a variety of frameworks and tools for its various features.

- Python is handling the backend server, such as requests, and responses to the quote & openAI API. 
  - Flask: A lightweight web framework for Python.
  - Jinja: A web template engine for Python.
  - Gunicorn: Python Web Server Gateway Interface HTTP server.
- JavaScript is handling mostly front-end, such as creating `bubble` elements, and playing the corresponding soundtrack when the `button` is clicked.
  - It is also communicates with the back-end for the AI chatbot, which I will talk about in-depth in the next section.
- Bootstrap: CSS framework for styling.
- Heroku: A cloud PAAS (platform as a service) supporting several programming languages. Used to deploy the website.

## 🌊 Challenges we ran into
- I encountered a problem when I tried to integrate the AI chatbot into TherAPI. Since I decided to use Flask because of the tight deadline for this hackathon, I noticed that in order to render the chat response, Flask forces you to render/refresh the whole page. Upon research, I came across a solution that I liked. The solution is to have JavaScript handle the message. Essentially, JavaScript takes the user's input and sends an AJAX request to the Flask server. The Flask server then receives the request and sends the message to the OpenAI server. The messages are stored on the local machine, and the Flask server returns the respond value in JSON format.
- Another challenge was the soundtrack autoplay. Apparently, many browsers have blocked the autoplay feature since 2011. In order to enable it, each user has to configure their browser. Fortunately, any kind of interaction with the website can trigger the sound to play. I created a play button that triggers the JavaScript function to play the sound when clicked.

## 🚀 Accomplishments that we're proud of
I'm proud of creating a useful website that is both technical and visually appealing for individuals to use in such a short period of time. I'm really happy with how TherAPI turned out as it is now.

## ✨ What we learned
Through the workshops, I learned various skills. I especially liked the Data-Driven Approaches to Societal Challenges by Dr. Padhu, even though I didn't see myself working in the data science field. I got a couple of great ideas for my next project through this workshop. As for building TherAPI, I learned how to manage my time so that I can be as productive as possible. It was also my first time working with an AI model. I really enjoyed participating in this hackathon.

## 📌 What's next for TherAPI
Countless new ideas:
- Adding more images and soundtracks for each theme!
- Creating a database to save users' messages to resume on the next "session."
- Implementing a user-to-user messaging system using Web-Socket, where users can join a "room" to have the same shared session.
- Adding more themes and customizable themes.
- Customizable chatbot.
- Upgrading the style!
And more. I really learned a lot and had fun during this hackathon. I want to thank everyone who took part in this hackathon.
