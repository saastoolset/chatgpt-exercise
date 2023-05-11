from nicegui import ui


def calculate_bmi(weight, height):
    # BMI calculation formula
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# with ui.Window("BMI Calculator"):
# Input fields for weight and height with nicegui
# weight = ui.input(label="Weight (kg)", type=float)
# height = ui.input(label="Height (m)", type=float)


weight = ui.input(label="Weight (kg)")
height = ui.input(label="Height (m)")

# @ui.call('Calculate BMI')
def on_calculate_bmi():
    w = float(weight.value)
    h = float(height.value)
    bmi = calculate_bmi(w, h)
    # Changed, ui.alert(f"Your BMI is: {bmi}")
    ui.notify(f"Your BMI is: {bmi}")

# Added, button to calculate BMI
ui.button('Calc!', on_click=on_calculate_bmi)

ui.run()

# Path: nicegui\app.py
# 1. TypeError: dataclass_transform() got an unexpected keyword argument 'field_specifiers' 
#   upgrade pip
    #   pip install --upgrade pip
#   pip uninstall nicegui
#   pip install nicegui

# 2. Component and parameter error
# from nicegui import ui

