from flask import Flask, render_template, request, jsonify
import re
from collections import defaultdict

app = Flask(__name__)

# Load and process corpus (book.txt)
with open('book.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = re.findall(r'\w+', text)

# Build frequency dictionary
word_freq = defaultdict(int)
for word in words:
    word_freq[word] += 1

# Total words
total_words = sum(word_freq.values())

# Calculate probabilities
probabilities = {word: freq / total_words for word, freq in word_freq.items()}

# Suggest top N matches for a given prefix
def suggest_words(prefix, top_n=5):
    prefix = prefix.lower()
    suggestions = {word: prob for word, prob in probabilities.items() if word.startswith(prefix)}
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_suggestions[:top_n]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    prefix = request.form['text']
    suggestions = suggest_words(prefix)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
