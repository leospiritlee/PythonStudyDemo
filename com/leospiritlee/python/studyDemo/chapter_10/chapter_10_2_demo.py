import json
def greet_user():
    file_name = 'username_v2.json'
    try:
        with open(file_name) as file_obj:
            user_name = json.load(file_obj)
    except FileNotFoundError:
        user_name = input('What is your name? ')
        with open(file_name,'w') as file_obj:
            json.dump(user_name,file_obj)
            print('We will remember you when yu come back,' + user_name + '!')
    else:
        print('Welcome back, ' + user_name + '!')

def get_stored_username():
    file_name = 'username_v2.json'
    try:
        with open(file_name) as file_obj:
            user_name = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name

def greet_user_v2():
    user_name = get_stored_username()
    if user_name:
        print('Welcome back, ' + user_name + '!')
    else:
        user_name = input('What is your name? ')
        file_name = 'username_v2.json'
        with open(file_name, 'w') as file_obj:
            json.dump(user_name, file_obj)
            print('We will remember you when yu come back,' + user_name + '!')

greet_user_v2()