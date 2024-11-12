from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/calculate')
def calculation():
    num1 = request.args.get("number1", type=int)
    num2 = request.args.get("number2", type=int)
    operation = request.args.get('operator')
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num1 == 0 or num2 == 0:
            return jsonify({"error":"Cannot divide with zero"})
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"})

    return jsonify({"result": result})



@app.route('/')
def clock():
    return render_template('index.html')


@app.route('/<filename>')
def file(filename):
    return app.send_static_file(filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)