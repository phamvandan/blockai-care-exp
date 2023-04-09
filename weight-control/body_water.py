# Watson Formula

def estimate_tbw(gender, age, height, weight):
    if gender == 'male':
        tbw = 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)
    elif gender == 'female':
        tbw = -2.097 + (0.1069 * height) + (0.2466 * weight)
    else:
        return {"Message": 'Invalid gender input. Please enter either "male" or "female".'}

    return tbw

# Example usage:
male_tbw = estimate_tbw('male', 35, 175, 75)
print(f"The estimated total body water for a 35-year-old male weighing 75 kg and 175 cm height is {male_tbw:.2f} liters.")

female_tbw = estimate_tbw('female', 28, 160, 62)
print(f"The estimated total body water for a 28-year-old female weighing 62 kg and 160 cm height is {female_tbw:.2f} liters.")
