from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/convert_to_fahrenheit')
def convert_to_fahrenheit():
    c = request.args.get('Temperature')
    f = int(c) * (9/5) + 32
    return {"Fahrenheit": f}


@app.route('/')
def clock():
    return render_template('index.html')


@app.route('/<filename>')
def file(filename):
    return app.send_static_file(filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)