from flask import Flask, url_for,request
from flask import render_template as rt
from twitter import proceed
app = Flask(__name__)

#Test
# @app.route('/')
# @app.route('/cj')
# def hello_world():
#     return rt('home.html')

# @app.route('/about')
# def about():
#     return "<h1>Hello About</h1>"

@app.route('/')
def index_page():
	return rt('index.html')

@app.route('/main', methods = ['POST', 'GET'])
def dashboard():
	if request.method:
		return rt('main.html')

@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
		t_id = request.form['twitterid']
		t_snt = proceed(t_id)
		return rt('result.html', id = t_id, values = t_snt, iurl = '/static/images/new_plot.png'  )

if __name__ == "__main__":
    app.run(debug=True)