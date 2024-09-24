#Initialize the accumulator.
total=0
#Get the bugs collefcted for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)
    #Input the number of bugs
    bugs= int(input())
    #Add bugs to total.
    total+= bugs

#Display the total bugs.
print('You collected a total of ',total, 'bugs.')

#Write a program that uses a loop displays the number of calories burned after 10,15,20,25,30 mins

calories_per_min=4.2 #Calories burned per min 
target_min={10,15,20,25,30}#Mins selected
#loop used for the problem
for min in target_min:
    calories_burned= min  *  calories_per_min
    print(f"Calories burned after {min} minutes: {calories_burned:.2f}")

#Write a program that asks the user  to enter the amount that they have budgeted for a month
budget=float(input("Enter your monthly budget:$ "))
num_expenses=int(input('How many expenses do you want to enter? '))
total_expenses=0

for i in range(num_expenses):
    expense= float(input(f'Enter expense {i + 1}:$ '))
    total_expenses+=expense

    difference=budget-total_expenses

if difference > 0:
    print(f"You are under budget by ${difference:.2f}.")
elif difference < 0:
    print(f"You are over budget by ${abs(difference):.2f}.")
else:
    print("You are exactly on budget.")

#Write a program that ask the user for the speed of a vehicle and the number of hours it has traveled.
speed = float(input('What is the speed of the vehicle in mph?: '))
num_hours = int(input('How many hours has it traveled?: '))
distance = 0


for i in range(1, num_hours + 1):  
    distance += speed  
    print(f'After hour {i}, the vehicle has traveled {distance} miles.')


#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
num_years = int(input("Enter the number of years: "))
total_rainfall = 0
num_months = 0

for year in range(1, num_years + 1):
    print(f"\nYear {year}:")
    
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        num_months += 1

average_rainfall = total_rainfall / num_months if num_months > 0 else 0

print(f"\nTotal number of months: {num_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")


#Write a program that displays a table of the Celsius Temp 0-20 and their fahrenheit equivalents.
print("Celsius\tFahrenheit")
print("-----------------------")

for celsius in range(0, 21):
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}\t{fahrenheit:.2f}")

#Write a program that calculates the amount of money a person would earn over a period of time if their salary is one penny the first day, two pennies the second day andd continues to double.
num_days = int(input("Enter the number of days: "))
daily_salary = 0.01
total_pay = 0.0

print("Day\tSalary ($)")
print("-------------------")

for day in range(1, num_days + 1):
    print(f"{day}\t{daily_salary:.2f}")
    total_pay += daily_salary
    daily_salary *= 2

print("-------------------")
print(f"Total pay over {num_days} days: ${total_pay:.2f}")


#Write a program with a loop that ask the user to enter a series of postive numbers.
#A negative number to end it 
#Then add them all together 
total = 0

while True:
    number = float(input("Enter a positive number (or a negative number to end): "))
    if number < 0:
        break
    total += number

print(f"The sum of the positive numbers is: {total:.0f}")

#Assuming the ocean's level is currently rising at about 1.6mm per year, create an application that displays the number of mm after each year.
rise_per_year = 1.6

print("Year\tOcean Level Rise (mm)")
print("----------------------------")

for year in range(1, 26):
    rise = rise_per_year * year
    print(f"{year}\t{rise:.1f}")


# At one college, the tuition for a full time student is 8k per semester.
#Tuition will increase by 3 percent each year for the next 5 years.
#write a program with a loop that displays the projected semester tuition amount for the next 5 years.
tuition = 8000
increase_rate = 0.03

print("Year\tTuition Amount")
print("---------------------")

for year in range(1, 6):
    tuition *= (1 + increase_rate)
    print(f"{year}\t${tuition:.2f}")


