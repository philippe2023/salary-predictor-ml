from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/method')
def method():
    return render_template('method.html')

@app.route('/analytics')
def analyse():
    return render_template('analytics.html')

@app.route('/predictor')
def predict():
    return render_template('predictor.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)