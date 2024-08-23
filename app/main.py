from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def services():
    return render_template('service.html')

@app.route('/why.html')
def why():
    return render_template('why.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
