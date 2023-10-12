def calculate_car_insurance_rate(age, gender, car_model, coverage_type):
    base_rate = 1000  # Base insurance rate

    # Age factor
    if age < 25:
        age_factor = 1.5
    else:
        age_factor = 1.0

    # Gender factor
    if gender == 'male':
        gender_factor = 1.2
    else:
        gender_factor = 1.0

    # Car model factor
    if car_model == 'sports':
        car_model_factor = 1.5
    else:
        car_model_factor = 1.0

    # Coverage type factor
    if coverage_type == 'comprehensive':
        coverage_factor = 1.5
    else:
        coverage_factor = 1.0

    # Calculate the final insurance rate
    insurance_rate = base_rate * age_factor * gender_factor * car_model_factor * coverage_factor
    return insurance_rate

# Get input from the user
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()
car_model = input("Enter your car model (e.g., sedan, sports): ").lower()
coverage_type = input("Enter your coverage type (e.g., liability, comprehensive): ").lower()

# Calculate and display the insurance rate
insurance_rate = calculate_car_insurance_rate(age, gender, car_model, coverage_type)
print(f"Your car insurance rate is: ${insurance_rate:.2f}")
