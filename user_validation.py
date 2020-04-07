import random
import string


def accept_user_info(first_name, last_name):
    return first_name+' '+last_name


def show_user_details():
    user_db = [accept_user_info(firstname, lastname)]
    for r in user_db:
        print(r)


def generate_user_password(a, b):
    user_full_name = str(accept_user_info(a, b))
    letters_remove1 = user_full_name[0:2]
    letters_remove2 = user_full_name[-2:]
    combine_letters = letters_remove1+letters_remove2
    # generating password using ascii letters
    letters = string.ascii_lowercase
    print(combine_letters + ''.join(random.choice(letters) for i in range(5)))


def create_new_password():

    password = input("Enter password: ")
    n = 1
    while n is 1:
        if len(password) < 7:
            print("Password must not be less than 7")
            password = input("Enter password: ")
        if len(password) >= 7:
            show_user_details()
            break


def accept_password(ans):
    if (ans == "no") or (ans == "n"):
        create_new_password()
    elif (ans == "y") or (ans == "yes"):
        show_user_details()
    else:
        print("""use 'yes/y' or 'no/n' """)


firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")

# generate password for user
generate_user_password(firstname, lastname)
# ask if user prefer password
print("Do you like your password: y/n")
ans = input("> ")
accept_password(ans)
