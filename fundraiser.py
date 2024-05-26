def get_contribtuors():
    contributors_firstname = []
    contributors_lastname = []
    amounts = []
    while len(contributors_firstname) < 4:
        name = input('\nWhat is your first and last name? (Separated by a space) ')
        if ' ' not in name:
            print('Please enter your first and last name separated by a space ')
            continue
        amount = int(input('How much would you like to donate? '))
        contributors_firstname.append(name.strip().split(' ')[0])
        contributors_lastname.append(name.strip().split(' ')[1])
        amounts.append(amount)
    return amounts, contributors_firstname, contributors_lastname

def get_acheivement():
    if 200 <= total_raised:
        statement = f'This means we can {contribution_levels[200]}!'
    elif 150 <= total_raised:
        statement = f'This means we can {contribution_levels[150]}!'  
    elif 100 <= total_raised:
        statement = f'This means we can {contribution_levels[100]}!'
    elif 50 <= total_raised:
        statement = f'This means we can {contribution_levels[50]}!'
    else:
        statement = 'We are almost there!'
    return statement

def find_contributor(amount_list, find_amount):
    contributor_index = []

    if amount_list.count(find_amount) == 0:
        return
    elif amount_list.count(find_amount) == 1:
        contributor_index.append(amount_list.index(find_amount))
    else:
        index = 0
        for amount in amount_list:
            if amount == find_amount:
                contributor_index.append(index)
            index += 1

    return contributor_index

organization_name = 'Little Paws Animal Shelter'
mission_statement = 'save abondoned and mistreated animals'
volunteer_name = 'Jennifer'
contribution_levels = {50 : 'provide two toys to our rescues', 100 : 'provide a bed for a rescued animal', 150 : 'provide one bag of food for our animal shelter', 200 : 'provide a pool for the animals'}
total_raised = 0

# Introduces organization and voluteer
print(f'Hello, my name is {volunteer_name} and I am raising money for {organization_name}. With your help we aim to {mission_statement}. \nSee the difference you can make with the following contribution levels:\n')

#Tells what levels of contribution will achieve
for i in contribution_levels:
    print(f'With your conrtibution of ${str(i)} we will {contribution_levels[i]}.')

# Gets name and donation amount for 4 contribtors and add amounts
list_amounts, firstnames, lastnames = get_contribtuors()
total_raised = sum(list_amounts)

#Display total raised
entry = 0
while entry < len(firstnames):
    print(f'\nThank you, {firstnames[entry]}! We appreciate your gift of ${list_amounts[entry]}.')
    entry += 1

#Display achievement
print(f'\nWith your help we have raised ${total_raised}.')
print(get_acheivement())

#Display max and min contributions
min_contribution = min(list_amounts)
max_contribution = max(list_amounts)

min_contributors = find_contributor(list_amounts, min_contribution)
max_contributors = find_contributor(list_amounts, max_contribution)

print(f'\nThe minimum contribution was ${min_contribution}. Made by:')
if len(min_contributors) == 0:
    print('No min contributors found.')
else:
    for contributor in min_contributors:
        print(f'\n{firstnames[contributor]} {lastnames[contributor]}')

print(f'\nThe maximum contribution was ${max_contribution}. Made by:')
if len(max_contributors) == 0:
    print('No max contributors found.')
else:
    for contributor in max_contributors:
        print(f'\n{firstnames[contributor]} {lastnames[contributor]}')
