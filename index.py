from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="template", static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    for element in request.files.getlist("file[]"):
        try:
            element.save("data/" + secure_filename(element.filename))
        except IsADirectoryError:
            return render_template("error.html")
    return render_template("success.html")


@app.route("/get_data")
def get_file():
    filename = "data/" + request.args.get('name')
    return send_file(filename)


@app.errorhandler(405)
def error_450(a):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
