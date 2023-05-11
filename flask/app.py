from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi_formula(weight, height)
        return render_template('result.html', bmi=bmi)
    return render_template('index.html')

def calculate_bmi_formula(weight, height):
    # BMI calculation formula
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# flask version is 0.12.2
# Mark when flask version > 1.0.2, https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask
# if __name__ == '__main__':
#     app.run(debug=True)
