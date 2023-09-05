from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('role.json', 'r') as file:
    roles_data = json.load(file)


@app.route('/')
def index():
    roles = [role_dict['Role'] for role_dict in roles_data]
    return render_template('index.html', roles=roles)


@app.route('/get_desc', methods=['POST'])
def get_desc():
    role_selected = request.form.get('role')
    for role_dict in roles_data:
        if role_dict['Role'] == role_selected:
            return jsonify(desc=role_dict['prompt'])
    return jsonify(desc="prompt not found.")


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


# if __name__ == "__main__":
 #   app.run(host='0.0.0.0', port=5000, debug=True)
