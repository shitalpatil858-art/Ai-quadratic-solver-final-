
from flask import Flask, request, render_template_string
import sympy as sp

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Quadratic Equation Solver</title>

    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #667eea, #764ba2);
            margin: 0;
            padding: 20px;
        }

        .box {
            max-width: 600px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        input {
            width: 90%;
            padding: 14px;
            font-size: 18px;
            margin: 10px;
            border-radius: 10px;
            border: 1px solid #aaa;
        }

        button {
            padding: 14px 25px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            background: #667eea;
            color: white;
        }

        .result {
            margin-top: 20px;
            text-align: left;
            background: #f2f2f2;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
</head>

<body>

<div class="box">

<h1>🧠 AI Quadratic Equation Solver</h1>

<p>Enter coefficients for ax² + bx + c = 0</p>

<form method="POST">

<input name="a" placeholder="Enter a" required>
<input name="b" placeholder="Enter b" required>
<input name="c" placeholder="Enter c" required>

<button type="submit">Solve Equation</button>

</form>

{% if result %}

<div class="result">
<h2>Solution</h2>
<pre>{{ result }}</pre>
</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        try:

            a = float(request.form["a"])
            b = float(request.form["b"])
            c = float(request.form["c"])

            D = b*b - 4*a*c

            x = sp.symbols("x")

            equation = a*x**2 + b*x + c

            roots = sp.solve(equation, x)

            result += f"Discriminant = {D}\n\n"

            if D > 0:
                result += "Nature: TWO DISTINCT REAL ROOTS\n"
            elif D == 0:
                result += "Nature: TWO EQUAL REAL ROOTS\n"
            else:
                result += "Nature: COMPLEX ROOTS\n"

            result += f"\nRoots = {roots}"

        except Exception as e:

            result = "Error: " + str(e)

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
