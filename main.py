from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# Function for time-based greeting
def get_greeting(name):
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good Morning"
    elif hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"
    return f"{greet}, {name}!"

# HTML Template
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World App</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background-color: #f2f2f2;
            margin-top: 100px;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0px 0px 10px gray;
        }
        button {
            padding: 10px 15px;
            margin: 5px;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>Hello World Web App</h2>

    <form method="post">
        <input type="text" name="username" placeholder="Enter your name" required>
        <br><br>
        <button type="submit" name="type" value="simple">Simple Hello</button>
        <button type="submit" name="type" value="enthusiastic">Enthusiastic</button>
        <button type="submit" name="type" value="formal">Formal</button>
    </form>

    {% if message %}
        <h3>{{ message }}</h3>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("username", "Guest")
        choice = request.form.get("type")

        base = get_greeting(name)

        if choice == "simple":
            message = f"Hello, {name}!"
        elif choice == "enthusiastic":
            message = f"HELLOOOO {name}!!! 🎉🔥"
        elif choice == "formal":
            message = f"Greetings, {name}. It is a pleasure to meet you."
        else:
            message = base

    return render_template_string(html_page, message=message)

if __name__ == "__main__":
    app.run(debug=True)
