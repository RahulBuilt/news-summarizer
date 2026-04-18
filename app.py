from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My news summarizer is coming soon."

if __name__ == "__main__":
    app.run(debug=True)