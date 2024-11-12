from flask import Flask, render_template, request
import requests
from tld import is_tld

app = Flask(__name__)


@app.route('/check_url')
def check_url():
    url = request.args.get('url')
    if is_tld(url.split('.')[-1]):

        try:
            response = requests.get(f'http://{url}', timeout=1)
            if response.status_code == 200:
                return {'status_code': 'OK'}
        except requests.exceptions.RequestException:
            return {'status_code': 'FAILED'}
    else:
        return {'status_code': 'INVALID'}

@app.route('/')
def clock():
    return render_template('index.html')


@app.route('/<filename>')
def file(filename):
    return app.send_static_file(filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)