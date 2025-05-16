from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'مرحباً بك في Vercel Flask API'})

@app.route('/hello')
def hello():
    name = request.args.get('name', 'زائر')
    return jsonify({'message': f'مرحباً، {name}!'})

# لا تضف app.run() عند النشر على Vercel
