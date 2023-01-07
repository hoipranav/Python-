print('''
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
██║     ██║██████╔╝███████║█████╗  ██████╔╝     
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝''')

def encrypt(shift,text):
    encrypted_word = ''
    index = 0    
    for i in text:
            index = ord(i) + shift
            encrypted_word += chr(index)
    print(f"Your Encoded Message is : {encrypted_word}\n\n")
def decrypt(shift,text):
    decrypted_word = ''
    for i in text:
            index = ord(i) - shift
            decrypted_word += chr(index)  
    print(f"Your Decoded Message is : {decrypted_word}\n\n")

def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode':
        encrypt(text = input("Type your message:\n"), shift = int(input("Type the shift number:\n")))
    elif direction == 'decode':
        decrypt(text = input("Type your message:\n"), shift = int(input("Type the shift number:\n")))

start()
while True:
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == 'yes':
        start()
    else:
        print("Thank you.!")
        break
