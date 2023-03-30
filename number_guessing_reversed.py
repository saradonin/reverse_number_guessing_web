from flask import Flask, request, render_template

app = Flask(__name__)

"""
WORK IN PROGRESS
"""

@app.route("/", methods=['POST', 'GET'])
def guess(min=1, max=1000):
    if request.method == "GET":
        return render_template("form.html")
    else:
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        guess = (max - min) // 2 + min
        # guess = int(request.form.get("guess", 500))
        answer = request.form.get("answer")

        if answer == "too big":
            max = guess
        elif answer == "too small":
            min = guess
        elif answer == "you win":
            return render_template("form.html", result="I won!")

        return render_template("form.html", guess=guess, min=min, max=max)




if __name__ == "__main__":
    app.run(debug=True, port=5000)

# curl -X GET localhost:5000/
# curl -X POST localhost:5000/