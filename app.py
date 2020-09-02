from flask import Flask, render_template

# Create flask app
app = Flask(__name__)

# Create index route so when go to URL, don't 404
@app.route('/')
def index():
    # Define what happens in this case
    return render_template('index.html')  # Don't need to specify templates folder

# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)