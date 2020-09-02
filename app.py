from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create flask app
app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # 3 slashes is relative loc. 4 slashes is absolute loc.
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


# Create index route so when go to URL, don't 404
@app.route('/')
def index():
    # Define what happens in this case
    return render_template('index.html')  # Don't need to specify templates folder

# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)