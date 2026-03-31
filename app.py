from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_ads = None

    if request.method == 'POST':
        n = int(request.form['n'])
        cost = list(map(int, request.form['cost'].split()))
        profit = list(map(int, request.form['profit'].split()))
        budget = int(request.form['budget'])

        # Prepare input for C++ program
        input_data = f"{n}\n"
        input_data += " ".join(map(str, cost)) + "\n"
        input_data += " ".join(map(str, profit)) + "\n"
        input_data += f"{budget}\n"

        # Run C++ program
        process = subprocess.Popen(
            ['./knapsack'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output, _ = process.communicate(input_data)
        output = output.strip().split("\n")

        result = output[0]
        if len(output) > 1:
            selected_ads = output[1]

    return render_template('index.html', result=result, selected_ads=selected_ads)

if __name__ == '__main__':
    app.run(debug=True)