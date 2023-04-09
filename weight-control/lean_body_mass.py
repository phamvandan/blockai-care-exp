# lean body mass Boer's Formula
def calculate_lean_body_mass(gender, weight, height):
    """
    Calculate lean body mass using the Boer's Formula.

    :param gender: 'male' or 'female'
    :param weight: weight in kg
    :param height: height in cm
    :return: lean body mass in kg
    """
    if gender == 'male':
        lbm = (0.407 * weight) + (0.267 * height) - 19.2
    elif gender == 'female':
        lbm = (0.252 * weight) + (0.473 * height) - 48.3
    else:
        return {"Message": 'Invalid gender input. Please enter either "male" or "female".'}

    return lbm

# Example usage:
lbm_male = calculate_lean_body_mass('male', 80, 180)
print(f"The estimated lean body mass for a 80 kg and 180 cm height male is {lbm_male:.2f} kg.")

lbm_female = calculate_lean_body_mass('female', 60, 165)
print(f"The estimated lean body mass for a 60 kg and 165 cm height female is {lbm_female:.2f} kg.")
