# is_present = False
# if is_present:
#     print('Start a lecture')
# else:
#     print("Skip a lecture")


# age = 18
# is_citizen = False
# has_passport = True
# if age >= 18 and is_citizen:
#     print('You are eligible to vote')
# elif not is_citizen and has_passport:
#     print('You are eligible to vote evethough you are not a citizen')
# else:
#     print('You are not eligible to vote')

monthly_income = int(input('Enter your monthly income: ')) #30,000
rent = int(input('Enter your monthly rent: ')) #10,000
takeout_budget = int(input('Enter your monthly takeout: ')) #4,000
actual_takeout = int(input('Enter your actual takeout: ')) #8,000
savings_goal = int(input('Enter your savings goal: ')) #5,000

if rent > monthly_income * 0.3:
    print('Your rent is eating your paycheck like an hungry hippo')
elif monthly_income - rent - actual_takeout< savings_goal:
    print('Your saving goal is more of a saving fantasy at this rate')
else:
    print('Your budget is actually balanced! Are you wizard?')
