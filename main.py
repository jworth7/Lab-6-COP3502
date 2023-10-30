#Jack Worth
def encode(password):
    new_password = ''
    for i in range(0,len(password)):
        new_password = new_password + str(int(password[i])+3)
    return new_password

def decode(password):#Kyle Schipf decode function
    original_pass = ''
    condition = True
    index = 0
    while condition:
        if(index == len(password)) or index == len(password) + 1:
            break
        if int(password[index]) <= 2:
            converted_num = str(int(password[index + 1]) + 7)
            original_pass += converted_num
            index += 2
        else:
            original_pass += str(int(password[index]) - 3)
            index += 1
    return original_pass


def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
    a = input('Please enter an option: ')
    return a

def main():
    condition = True
    stored_pass = ''
    while condition:
        selection = menu()
        if selection == '1':
            first_pass = input('Please enter your password to encode: ')
            stored_pass = encode(first_pass)
            print('Your password has been encoded and stored!\n')
        elif selection == '2':
            print('The encoded password is ' + stored_pass, end=', ')
            original_pass = decode(stored_pass)
            print('and the original password is ' + original_pass + '\n')
        else:
            break

if __name__ == '__main__':
    main()