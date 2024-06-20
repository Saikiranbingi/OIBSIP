def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator")
    
    # Prompt user for weight and height
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))
    
    # Calculate BMI
bmi = calculate_bmi(weight, height)
    
    # Classify BMI
category = classify_bmi(bmi)
    
    # Display result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")

