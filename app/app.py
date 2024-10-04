import openai
import time
from questions import LIST_QUESTIONS
from flask import Flask, render_template, request, jsonify
from config import API_KEY, GPT_MODEL
app = Flask(__name__)

openai.api_key = API_KEY
chatlog = []

@app.route('/')
def index():
    return render_template('index.html', LIST_QUESTIONS=LIST_QUESTIONS, chatlog=chatlog)

@app.route('/generate', methods=['POST'])
def generate():
    start_time = time.time()
    user_response = request.form['prompt']
    chatlog.append({"role": "user", "content": user_response})
    
    completion = openai.ChatCompletion.create(
        model= GPT_MODEL,
        messages=chatlog,
        max_tokens = 1024,
        temperature = 0
    )
    response = completion.choices[0].message.content

    chatlog.append({"role": "assistant", "content": response})
    
    end_time = time.time()
    response_time = end_time - start_time
    print(f"Response Time: {response_time:.2f} seconds") 
    return jsonify(chatlog[-1])

if __name__ == '__main__':
    app.run(debug=True)