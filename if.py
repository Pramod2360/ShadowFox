def bmi_category(height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    if bmi >= 30:
        return "Obesity"
    elif bmi >= 25:
        return "Overweight"
    elif bmi >= 18.5:
        return "Normal"
    else:
        return "Underweight"

# Example
print("BMI example (1.75m,70kg):", bmi_category(1.75, 70))
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
def find_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None
city = "Abu Dhabi"
c = find_country(city)
print(f"\n{city} is in {c}")
def same_country(city1, city2):
    c1 = find_country(city1)
    c2 = find_country(city2)
    if c1 and c2 and c1 == c2:
        return f"Both cities are in {c1}"
    else:
        return "They don't belong to the same country"

print(same_country("Mumbai", "Chennai"))
print(same_country("Sydney", "Dubai"))
