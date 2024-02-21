import Caesar_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = True

while restart:
    print(Caesar_art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    def cipher(code_direction, code_text, code_shift):
        message = ""
        encrpyt_decrypt = "encrypted"
        if "encode" not in code_direction:
            encrpyt_decrypt = "decrypted"
        if code_direction == "decode":
                code_shift *= -1
        for char in code_text:
            if char in alphabet:
                shift_letter = alphabet.index(char)
                shift_amount = shift_letter + code_shift
                if shift_amount > 25:
                    shift_amount -= 26
                if shift_amount < 0:
                    shift_amount  += 26
                message += alphabet[shift_amount]
            else:
                message += char
        print(f"Here is your {encrpyt_decrypt} message: {message}")    
        
    cipher(code_direction=direction, code_text=text, code_shift=shift)

    user_answer = input("Would you like to restart the cipher program? \n").lower()
    if user_answer == "no":
        restart = False
    