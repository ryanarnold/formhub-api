from flask import Flask, jsonify, request, url_for
from flask_cors import CORS

FORM_TEMPLATES_DIR = './static/form_templates'

app = Flask(__name__)
CORS(app)

@app.route('/submission', methods=['POST'])
def index():
    data = request.json
    user_data = data['user_data']
    forms = data['forms']

    json_response = {
        'generated_forms': []
    }

    for form in forms:
        generated_form = {}
        generated_form['link'] = url_for('static', filename=f'form_templates/{form}.pdf')
        generated_form['id'] = form

        json_response['generated_forms'].append(generated_form)

    return jsonify(json_response)