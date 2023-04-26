from flask import Flask, render_template
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/chatbot/<prompt>")
def chatbot(prompt):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=prompt,
                                      n=1,
                                      temperature=0.6,
                                      max_tokens=2500,
                                      stop=None)
  return response["choices"][0]['text']

if __name__ == "__main__":
  app.run(debug=True)
