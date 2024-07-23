def encode(password):
    enc = ''
    for i in range(len(password)):
        enc += str(int(password[i])+3)
    return enc

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    opt = input("Please enter an option: ")

    if opt == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!")
    if opt == 2:
        continue
    if opt == 3:
        break