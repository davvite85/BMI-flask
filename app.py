from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>BMI Calculator</h1>
    <form action="/calculate" method="get">
      Weight (kg): <input name="weight"><br>
      Height (cm): <input name="height"><br>
      <input type="submit" value="Calculate BMI">
    </form>
    """

@app.route("/calculate")
def calculate():
    try:
        weight = float(request.args.get("weight", 0))
        height_cm = float(request.args.get("height", 0))
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return f"<h2>Your BMI is: {bmi:.2f}</h2>"
    except:
        return "<h2>Invalid input. Please enter numbers only.</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
