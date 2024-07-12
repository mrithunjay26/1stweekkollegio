from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key='sk-proj-MuaWKbA6rDIYqtkuRmX4T3BlbkFJPNkr2FkdxTlqmz9Gbvgx')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.form['user_message']

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        ai_message = response.choices[0].message.content

        return jsonify({'ai_message': ai_message})

    except KeyError as e:
        return jsonify({'error': f'Missing key in request: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
