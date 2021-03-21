import Art

print(Art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(var_text, shift_amount):
    
    encrypted_word = ''
    for letter in var_text:
        if letter in alphabet:
            new_index = int(
                        (alphabet.index(letter)+shift_amount)
                        %
                        (len(alphabet)-1)
                        )
            encrypted_word += alphabet[new_index]
        else:
            encrypted_word += letter
        
    print(f'Your encrypted word: {encrypted_word}')

def decrypt(var_text, shift_amount):
    
    decrypted_word = ''
    for letter in var_text:
        if letter in alphabet:     
            new_index = int(
                        (alphabet.index(letter)-shift_amount)
                        %
                        (len(alphabet)-1)
                        )
            decrypted_word += alphabet[new_index]
        else:
            decrypted_word += letter
        
    print(f'Your decrypted word: {decrypted_word}')

while True:    
    direction = input("Type 'encode' to encrypt\n"
                      "Type 'decode' to decrypt\n"
                      "Type 'quit' to quit programm\n")
    
    #Encryption
    if direction[0].lower() == 'e':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text,shift)
    
    #Decryption
    elif direction[0].lower() == 'd':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text,shift)
    
    #Quit    
    elif direction[0].lower() == 'q':
        print('Quitting')
        break
    
    #Unknown command
    else:
        print('Unknown command.')
    