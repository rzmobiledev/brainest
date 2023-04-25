'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''


def encrypt(key, messages):
    messages = messages.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''

    for message in messages:
        if message in letters:
            message_index = (letters.find(message) + key) % len(letters)
            res = res + letters[message_index]
        else:
            res = res + message
    
    print(res)


def decrypt(key, messages):
    messages = messages.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''

    for message in messages:
        if message in letters:
            message_index = (letters.find(message) - key) % len(letters)
            res = res + letters[message_index]
        else:
            res = res + message
    
    print(res)
    

while True:

    user_input = input("Do you want to (e)ncrypt or (d)ecrypt?: ")

    try:
        
        if user_input == 'e' or user_input == 'E':
            key = int(input("Please enter the key (0 to 25) to use: "))

            # key length maximum 25 chars
            if key > 25:
                print("Maximum key is 25!")
                continue
            
            msg = input("Enter the message to encrypt: ")
            encrypt(key, msg)
        
        elif user_input == 'd' or user_input == 'D':
            key = int(input("Please enter the key (0 to 25) to use: "))

            # key length maximum 25 chars
            if key > 25:
                print("Maximum key is 25!")
                continue
            
            msg = input("Enter the message to decrypt: ")
            decrypt(key, msg)
        
        elif user_input == 'done' or user_input == 'Done':
            break

        elif user_input != 'e' or user_input != 'd':
            print("Wrong input! choose only `e` or `d`")
            continue
    
    except ValueError:
        print("Wrong value. Please put number between 0 - 25!")
        continue

    except Exception as e:
        print(str(e))
