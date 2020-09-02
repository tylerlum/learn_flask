from flask import Flask

# Create flask app
app = Flask(__name__)

# Create index route so when go to URL, don't 404
@app.route('/')
def index():
    # Define what happens in this case
    return "Hello, World!"

# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)