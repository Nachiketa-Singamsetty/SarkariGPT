from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import summarize_document
from fake_detector import detect_fake_news
from fact_checker import fact_check_text

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    result = summarize_document(text)
    return jsonify(result)

@app.route('/detect_fake', methods=['POST'])
def detect_fake():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    result = detect_fake_news(text)
    return jsonify(result)

@app.route('/fact_check', methods=['POST'])
def fact_check():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    result = fact_check_text(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 