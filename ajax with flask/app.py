from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_get_data/', methods=['GET'])
def _get_data():
    return jsonify({'data1': 89,'data2': 92})


if __name__ == "__main__":
    app.run(debug=True)