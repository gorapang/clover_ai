from flask import Flask, request, jsonify
import os
import openai
import json
from Config import OPENAI_API_KEY


app = Flask(__name__)

openai.api_key = OPENAI_API_KEY

@app.route('/hello', methods=['GET'])
def hello_flask():
    return "hello, flask!"


@app.route('/image_verify', methods=['POST'])
def image_verify():
    image_url = request.form['image']	
    print(image_url)

    openai.api_key = OPENAI_API_KEY
    client = openai.OpenAI(
        api_key=OPENAI_API_KEY
    ) 

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "이 이미지가 쓰레기봉투의 이미지면 'success', 아니면 'fail'를 출력해줘."},
                    {
                        "type": "image_url",
                        "image_url": image_url
                    },
                ]
            }
        ],
        max_tokens=10
    )

    result = response.choices[0].message.content
    print(result)
    return jsonify({"result": result}) # Yes or No 


if __name__ == "__main__":
		app.run()