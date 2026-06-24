** MINI_PROJECTS(PYTHON FUNDAMENTALS)**
Objective:-

**Create a Python program that asks the user for the distance they want to travel and suggests an appropriate mode of transportation based on the distance.

Rules
Less than 3 miles → Bicycle
3 to 299 miles → Motor-Cycle
300 miles or more → Super-Car**

Python Code:-

def suggest_vehicle(distance):
    if distance < 3:
        return "Bicycle"
    elif distance < 300:
        return "Motor-Cycle"
    else:
        return "Super-Car"


try:
    distance = float(input("How far would you like to travel (in miles)? "))

    if distance < 0:
        print("Distance cannot be negative.")
    else:
        vehicle = suggest_vehicle(distance)
        print(f"I suggest {vehicle} to your destination.")

except ValueError:
    print("Please enter a valid numeric distance.")
Sample Output 1
How far would you like to travel (in miles)? 2

I suggest Bicycle to your destination.
Sample Output 2
How far would you like to travel (in miles)? 150

I suggest Motor-Cycle to your destination.
Sample Output 3
How far would you like to travel (in miles)? 2500

I suggest Super-Car to your destination.


Objective

**A cloud hosting provider charges $0.51 per hour for running a server. Calculate:

Cost to operate one server per day
Cost to operate one server per week
Cost to operate one server per month (30 days)
Number of days a server can operate with a budget of $918
Formulae
Cost per Day = Hourly Cost × 24
Cost per Week = Cost per Day × 7
Cost per Month = Cost per Day × 30
Days with $918 = 918 ÷ Cost per Day**

Python Program
# Cloud Server Cost Calculator

hourly_cost = 0.51

# Cost calculations
daily_cost = hourly_cost * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30

# Budget calculation
budget = 918
days_operated = budget / daily_cost

# Display results
print("Cost to operate one server per day: $", round(daily_cost, 2))
print("Cost to operate one server per week: $", round(weekly_cost, 2))
print("Cost to operate one server per month: $", round(monthly_cost, 2))
print("Number of days a server can operate with $918:", round(days_operated, 2))
Sample Output
Cost to operate one server per day: $ 12.24
Cost to operate one server per week: $ 85.68
Cost to operate one server per month: $ 367.20
Number of days a server can operate with $918: 75.00