temperature = 35

if temperature > 30:
    print('It\'s hot outside!')
    print('Stay hydrated.')

print('Have a great day!')




age = 15

if age >= 18:
    print('You can vote!')
else:
    print('You\'re too young to vote.')
    years_left = 18 - age
    print(f'Come back in {years_left} years.')





score = 85

if score >= 60:
    print('You passed!')
else:
    print('You failed.')




has_ticket = True
age = 14

if has_ticket:
    if age >= 12:
        print('Welcome to the ride!')
    else:
        print('Sorry, you must be 12 or older.')
else:
    print('You need a ticket first.')
  



age = 20

if age >= 18:
    status = 'adult'
else:
    status = 'minor'
print(status)
status = 'adult' if age >= 18 else 'minor'
print(status)