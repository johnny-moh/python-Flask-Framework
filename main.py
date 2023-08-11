from flask import Flask
app = Flask(__name__)
from routes import *

@app.route('/')

@app.route('/portfolio')

def portfolio():
   projects =[
              { 'id': 123, 'title': 'Title 1', 'description': 'About Title 1'}]
   return render_template('portfolio.html')
   