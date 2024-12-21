from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/area_of_circle', methods=['POST'])
def area_of_circle():
    radius = float(request.form['radius'])
    area = math.pi * math.pow(radius, 2)
    return {"area": round(area, 2)}

@app.route('/marksheet', methods=['POST'])
def marksheet():
    marks = list(map(int, request.form['marks'].split(',')))  # Assume marks are passed as comma-separated values
    total = sum(marks)
    if len(marks) > 0:
        average = total / len(marks)
    else:
        average = 0
    return {"total": total, "average": round(average, 2)}

@app.route('/odd_even_detector', methods=['POST'])
def odd_even_detector():
    number = int(request.form['number'])
    if number % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return {"number": number, "result": result}

@app.route('/calculator', methods=['POST'])
def calculator():
    operation = request.form['operation']
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "undefined"
    else:
        result = "invalid operation"

    return {"result": result}

@app.route('/vowel_detector', methods=['POST'])
def vowel_detector():
    text = request.form['text']
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return {"vowel_count": count}

@app.route('/bmi_calculator', methods=['POST'])
def bmi_calculator():
    weight = float(request.form['weight'])
    height = float(request.form['height'])  # Height in meters
    if height > 0:
        bmi = weight / (height ** 2)
    else:
        bmi = 0
    return {"bmi": round(bmi, 2)}

@app.route('/multiplication_table', methods=['POST'])
def multiplication_table():
    number = int(request.form['number'])
    table = {}
    for i in range(1, 11):
        table[i] = number * i
    return {"table": table}

@app.route('/celsius_to_fahrenheit', methods=['POST'])
def celsius_to_fahrenheit():
    celsius = float(request.form['celsius'])
    fahrenheit = (celsius * 9 / 5) + 32
    return {"fahrenheit": round(fahrenheit, 2)}

@app.route('/sum_even_odd', methods=['POST'])
def sum_even_odd():
    numbers = list(map(int, request.form['numbers'].split(',')))  # Assume numbers are passed as comma-separated
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return {"even_sum": even_sum, "odd_sum": odd_sum}

if __name__ == "__main__":
    app.run(debug=True, port=5001)
