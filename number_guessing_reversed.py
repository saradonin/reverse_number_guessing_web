from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def postcode_valid():
    if request.method == "GET":
        return render_template("form.html")
    else:
        return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# curl -X GET localhost:5000/
# curl -X POST localhost:5000/