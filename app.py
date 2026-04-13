from flask import Flask, render_template

app = Flask(__name__)

@app.route("/weather")
def weather():

    temperatures = [35, 10, -3, 22, 18, 40]

    results = []

    for t in temperatures:

        if t < 0:
            status = "Cold"

        elif t <= 20:
            status = "Warm"

        else:
            status = "Hot"

        results.append({
            "temp": t,
            "status": status
        })

    return render_template(
        "weather.html",
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
