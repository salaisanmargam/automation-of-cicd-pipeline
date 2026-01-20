from flask import Flask, request, render_template_string

app = Flask(__name__)

feedbacks = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Feedback</title>
</head>
<body>
    <h2>Student Feedback Form</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Feedback: <input type="text" name="feedback" required><br><br>
        <button type="submit">Submit</button>
    </form>

    <h3>Submitted Feedback</h3>
    <ul>
        {% for f in feedbacks %}
            <li><b>{{f.name}}</b>: {{f.feedback}}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        feedbacks.append({
            "name": request.form["name"],
            "feedback": request.form["feedback"]
        })
    return render_template_string(HTML_PAGE, feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
