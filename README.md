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
- Programming Language: Python – Core logic and backend processing
  
- Web Framework/Backend: Flask – Lightweight Python web framework for serving the app
  
- Frontend :HTML5 – Structure of the web page (user interface)
           :CSS3 – Styling the UI with a clean, responsive look
           :JavaScript (Vanilla) – For making AJAX calls to the Flask backend

- NLP and Text Processing: Regular Expressions (re module) – Tokenization and word extraction
                         :collections.defaultdict – Efficient word frequency dictionary

- File Handling & Data: book.txt – Custom training corpus to build word frequencies

# How to Run the Program
Step 1: Clone or Download the Project
git clone https://github.com/your-username/keyboard-suggestion-app.git
cd keyboard-suggestion-app
Or download the ZIP file and extract it.

✅ Step 2: Add a Training File
Make sure a plain-text file named book.txt is present in the root directory.
You can use any text document as the data source for suggestions.

Example:

css
Copy
Edit
book.txt
├── Contains a large amount of English text (e.g., a book, article, or scraped content)
✅ Step 3: Set Up Python Environment
Ensure you have Python 3.7–3.13 installed.

Install Flask (if not already installed):

bash
Copy
Edit
pip install flask
✅ Step 4: Run the Flask Server
bash
Copy
Edit
python app.py
You should see output like:

csharp
Copy
Edit
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
✅ Step 5: Use the Application
Open your browser and go to:

👉 http://127.0.0.1:5000

Start typing in the input box.

Suggestions will appear based on your corpus in real-time.
