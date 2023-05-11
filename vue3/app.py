# Not work, miss link with vine

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    weight = float(request.json['weight'])
    height = float(request.json['height'])
    bmi = calculate_bmi_formula(weight, height)
    return jsonify({'bmi': bmi})

def calculate_bmi_formula(weight, height):
    # BMI calculation formula
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# if __name__ == '__main__':
#     app.run(debug=True)
