from flask import Flask, request, render_template

app = Flask(__name__)

"""
WORK IN PROGRESS
"""

@app.route("/", methods=['POST', 'GET'])
def guess():
    if request.method == "GET":
        return render_template("start.html")
    else:
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        answer = request.form.get("answer")
        # guess = (max - min) // 2 + min
        guess = int(request.form.get("guess", 500))

        if answer == "Too big":
            max = guess
        elif answer == "Too small":
            min = guess
        elif answer == "You win!":
            return render_template("win.html", guess=guess)

        guess = (max - min) // 2 + min

        return render_template("form.html", guess=guess, min=min, max=max)




if __name__ == "__main__":
    app.run(debug=True, port=5001)

# curl -X GET localhost:5001/
# curl -X POST localhost:5001/