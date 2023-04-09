def calculate_bmr(weight, height, age, gender):
    """
    Calculates Basal Metabolic Rate (BMR) using Harris-Benedict equation. (kcal/day)
    weight: weight in kg
    height: height in cm
    age: age in years
    gender: 'M' for male, 'F' for female
    """
    if gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'F':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        return {"Message": "Invalid gender. Please enter 'M' or 'F'."}
    
    return bmr

# Example usage
weight = 70 # kg
height = 170 # cm
age = 30 # years
gender = 'M'

bmr = calculate_bmr(weight, height, age, gender)
print("Your BMR is:", bmr, "kcal/day")
