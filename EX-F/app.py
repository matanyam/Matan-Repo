import json



from flask import Flask, render_template, request, jsonify
import requests
from tld import is_tld

app = Flask(__name__)


@app.route('/data_insert', methods=['GET'])
def data_insert():
    name = request.args.get('name')
    email = request.args.get('email')
    comment = request.args.get('comment')
    email_tld = email.split(".")[-1]
    if not is_tld(email_tld):
        return jsonify({"message": "Invalid domain"})
    else:
        with open("feedback.txt","a") as feedback:
            total_feedback = {
                "name": name,
                "email": email,
                "comment": comment
            }
            json.dump(total_feedback,feedback,indent=4)
            return jsonify({"message": "Feedback saved successfully"})




@app.route('/')
def clock():
    return render_template('index.html')


@app.route('/<filename>')
def file(filename):
    return app.send_static_file(filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)