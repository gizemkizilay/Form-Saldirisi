import sqlite3
import html
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    """Initializes the SQLite database with a single table for comments."""
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            comment_text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# --- HTML Templates (Embedded for single-file application) ---

# VULNERABLE TEMPLATE
# The | safe filter in Jinja2 tells the template engine NOT to auto-escape the content.
# This makes the application vulnerable to Stored Cross-Site Scripting (XSS).
VULNERABLE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vulnerable Comments</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .comment-box { border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
        .danger { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1><span class="danger">Vulnerable</span> Comment Section</h1>
    <p>Try submitting this script: <code>&lt;script&gt;alert('XSS Exploit!');&lt;/script&gt;</code></p>
    
    <form method="POST">
        <label for="author">Author:</label><br>
        <input type="text" id="author" name="author" required><br><br>
        
        <label for="comment_text">Comment:</label><br>
        <textarea id="comment_text" name="comment_text" rows="4" cols="50" required></textarea><br><br>
        
        <button type="submit">Submit</button>
    </form>
    
    <hr>
    <h2>Comments</h2>
    {% for comment in comments %}
        <div class="comment-box">
            <strong>{{ comment.author }}:</strong> 
            <!-- DANGER: 'safe' filter disables HTML escaping, executing any stored scripts -->
            <span>{{ comment.comment_text | safe }}</span>
        </div>
    {% else %}
        <p>No comments yet.</p>
    {% endfor %}
    
    <br><br>
    <a href="/secure">Go to Secure Version &rarr;</a>
</body>
</html>
"""

# SECURE TEMPLATE
# Implements client-side JavaScript validation.
# Server-side escaping already handles characters before they hit the DB.
SECURE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Comments</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .comment-box { border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
        .secure { color: green; font-weight: bold; }
    </style>
    <script>
        // Frontend Solution: Input Sanitization / Validation
        function validateForm() {
            var commentText = document.getElementById('comment_text').value;
            // Check for potentially dangerous characters (< and >)
            if (commentText.includes('<') || commentText.includes('>')) {
                alert("Security Alert: The characters '<' and '>' are not allowed in comments.");
                return false; // Prevent the form from submitting
            }
            return true; // Allow submission if clean
        }
    </script>
</head>
<body>
    <h1><span class="secure">Secure</span> Comment Section</h1>
    <p>Client-side validation and Server-side escaping prevent XSS attacks here.</p>
    
    <!-- onsubmit event triggers our JavaScript validation function -->
    <form method="POST" onsubmit="return validateForm()">
        <label for="author">Author:</label><br>
        <input type="text" id="author" name="author" required><br><br>
        
        <label for="comment_text">Comment:</label><br>
        <textarea id="comment_text" name="comment_text" rows="4" cols="50" required></textarea><br><br>
        
        <button type="submit">Submit</button>
    </form>
    
    <hr>
    <h2>Comments</h2>
    {% for comment in comments %}
        <div class="comment-box">
            <!-- Jinja2 escapes text by default, adding another layer of defense. -->
            <!-- Note: The text is already escaped in the database by our Python code. -->
            <strong>{{ comment.author }}:</strong> 
            <span>{{ comment.comment_text }}</span>
        </div>
    {% else %}
        <p>No comments yet.</p>
    {% endfor %}
    
    <br><br>
    <a href="/vulnerable">&larr; Go to Vulnerable Version</a>
</body>
</html>
"""

# --- Routes ---

@app.route('/')
def index():
    return redirect(url_for('vulnerable'))

@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    conn = sqlite3.connect('comments.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if request.method == 'POST':
        author = request.form['author']
        comment_text = request.form['comment_text']
        
        # VULNERABILITY: Saving user input directly to the database exactly as it is,
        # with absolutely no sanitization or escaping.
        c.execute('INSERT INTO comments (author, comment_text) VALUES (?, ?)', (author, comment_text))
        conn.commit()
        return redirect(url_for('vulnerable'))

    # Retrieve all comments
    c.execute('SELECT * FROM comments')
    comments = c.fetchall()
    conn.close()
    
    return render_template_string(VULNERABLE_TEMPLATE, comments=comments)

@app.route('/secure', methods=['GET', 'POST'])
def secure():
    conn = sqlite3.connect('comments.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if request.method == 'POST':
        author = request.form['author']
        raw_comment_text = request.form['comment_text']
        
        # SECURE: Backend Solution - Entity Escaping
        # Using html.escape() to convert characters like '<' to '&lt;' and '>' to '&gt;'
        # This prevents the browser from interpreting the input as executable HTML/JavaScript.
        sanitized_comment_text = html.escape(raw_comment_text)
        sanitized_author = html.escape(author) 
        
        c.execute('INSERT INTO comments (author, comment_text) VALUES (?, ?)', (sanitized_author, sanitized_comment_text))
        conn.commit()
        return redirect(url_for('secure'))

    # Retrieve all comments
    c.execute('SELECT * FROM comments')
    comments = c.fetchall()
    conn.close()
    
    return render_template_string(SECURE_TEMPLATE, comments=comments)


if __name__ == '__main__':
    # Initialize the DB before running the app
    init_db()
    # Run the application
    app.run(debug=True, port=5000)
