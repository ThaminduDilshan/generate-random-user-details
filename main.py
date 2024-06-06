import sys
import random
from faker import Faker

fake = Faker()

csv_headers = [
    'userName', 'firstName', 'lastName', 'middleName', 'formattedName', 'displayName', 'profileUrl', 'nickName', 
    'mobilePhoneNumber', 'activeStatus', 'accountLocked',
    'homeAddress_locality', 'homeAddress_postal', 'homeAddress_region', 'homeAddress_street', 'country',
    'locale', 'birthDate'
]

email_suffix = '@faketd.com'
gravatarBase = "https://robohash.org/mail@"


def getEmailAddress(firstname: str, num: int):

    username = firstname.lower() + str(num) + email_suffix
    return username


def getRandomGravatar(email: str):

    return gravatarBase + email


def generateUser(firstName: str, num: int):
    
    user = {}

    emailAddress = getEmailAddress(firstName, num)
    user['userName'] = emailAddress
    user['firstName'] = firstName
    user['lastName'] = fake.last_name()
    user['middleName'] = fake.first_name()
    user['formattedName'] = firstName + " " + user['middleName'] + " " + user['lastName']
    user['displayName'] = firstName + " " + user['lastName']
    user['profileUrl'] = getRandomGravatar(emailAddress)
    user['nickName'] = firstName.lower() + str(num)

    user['mobilePhoneNumber'] = fake.phone_number()
    user['activeStatus'] = bool(random.getrandbits(1))
    user['accountLocked'] = bool(random.getrandbits(1))
    
    user['homeAddress_locality'] = fake.city()
    user['homeAddress_postal'] = fake.postcode()
    user['homeAddress_region'] = fake.state()
    user['homeAddress_street'] = fake.street_address()
    user['country'] = fake.country()

    user['locale'] = fake.locale()
    user['birthDate'] = fake.date_of_birth(minimum_age=18, maximum_age=65)
    
    return user


# Main program.
if __name__ == '__main__':

    # Get the number of users to generate.
    count = int(sys.argv[1])
    user_list = []

    # Generate unique first names.
    names = [fake.unique.first_name() for i in range(count)]
    assert len(set(names)) == len(names)

    # Generate users.
    for i in range(count):
        user = generateUser(names[i], i)
        user_list.append(user)
    
    # Write to CSV.
    with open('users.csv', 'w') as f:
        f.write(','.join(csv_headers) + '\n')
        for user in user_list:
            f.write(','.join([str(user[key]) for key in csv_headers]) + '\n')
