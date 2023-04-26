from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)

def chatbot(prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        n=1,
                                        temperature=0.6,
                                        max_tokens=2500,
                                        stop=None)
    return response["choices"][0]['text']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']
        AI_response = chatbot(message)
        return render_template('home.html', AI_response=AI_response)
    else:
        return render_template('home.html', AI_response='')

if __name__ == '__main__':
    app.run(debug=True)
