def encode(password):
    enc = ''
    for i in range(len(password)):
        enc += str(int(password[i])+3)
    return enc
def decode(password):
    dec = ''
    for num in password:
        if int(num) > 2:
            dec += str(int(num) - 3)
        else:
            dec += str(int(num) + 7)
    return dec

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    opt = int(input("Please enter an option: "))

    if opt == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!")
    if opt == 2:    
        print("The encoded password is ", encoded_password, ", the original password is ", decode(encoded_password))
    if opt == 3:
        break
