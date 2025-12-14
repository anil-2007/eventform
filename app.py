from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # print("New Contact Message")
        # print("Name:", name)
        # print("Email:", email)
        # print("Message:", message)

        # 🔽 Write to a text file
        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
            f.write("-" * 40 + "\n")

        return "🚀 Successfully! Your message was sent."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
