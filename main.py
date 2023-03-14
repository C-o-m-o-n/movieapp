from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
import requests
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  movies='all'
  movie_search='all'
  if request.method == 'POST':
    movie_search = request.form['search']
    url = f'http://www.omdbapi.com/?apikey=be3d2cec&s={movie_search}'
    resp = requests.get(url)
    movies = resp.json()
  return render_template('index.html', movies=movies, movie_search=movie_search)
  
if __name__ =='__main__':
  app.run(debug=True)