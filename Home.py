from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('Home Page.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("Result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
