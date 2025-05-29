# NLP_Keyword_Suggestion
A simple NLP-powered web application that provides intelligent word suggestions as you type, trained on a custom corpus

---

# How It Works
- book.txt is read and tokenized using regular expressions
- A frequency dictionary of all words is built
- When user types a prefix like "pro", the app:
- Finds all words starting with that prefix
- Sorts them by probability (frequency / total words)
- Returns top 5 suggestions

---

# Tools Used
- **Programming Language**  
  Python – Core logic and backend processing

- **Web Framework / Backend**  
  Flask – Lightweight Python web framework for serving the app

- **Frontend**
  - HTML5 – Structure of the web page (user interface)
  - CSS3 – Styling the UI with a clean, responsive look
  - JavaScript (Vanilla) – For making AJAX calls to the Flask backend

- **NLP and Text Processing**
  - Regular Expressions (`re` module) – Tokenization and word extraction
  - `collections.defaultdict` – Efficient word frequency dictionary

- **File Handling & Data**
  - `book.txt` – Custom training corpus to build word frequencies

---


# How to Run the Program
- Clone or Download the Project
git clone https://github.com/Shalini-Majumdar/NLP_Keyword_Suggestion.git

- Add a Training File: Make sure a plain-text file named book.txt is present in the root directory.

- Ensure you have Python 3.7–3.13 installed.

- Install Flask and Run the Flask Server: python app.py

- Open your browser and go to: http://127.0.0.1:5000
