from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    age = int(request.form['age'])
    gender = request.form['gender']
    car_model = request.form['car_model']
    coverage_type = request.form['coverage_type']

    # Your insurance rate calculation logic here (similar to the previous Python example)
    base_rate = 1000
    # Calculate insurance_rate based on input variables

    return jsonify({'insurance_rate': base_rate})

if __name__ == '__main__':
    app.run(debug=True)
