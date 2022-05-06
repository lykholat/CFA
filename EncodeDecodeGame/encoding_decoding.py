from string import ascii_lowercase
import random



def create_code():
    codes=set()

    while len(codes) < len(ascii_lowercase):
        new_code=random.choice(ascii_lowercase).upper()+random.choice(ascii_lowercase).upper()+random.choice(ascii_lowercase).upper()
        codes.add(new_code)
    
    #code for spaces
    new_code=random.choice(ascii_lowercase).upper()+random.choice(ascii_lowercase).upper()+random.choice(ascii_lowercase).upper()
    codes.add(new_code)

    codes=list(codes)
    code_dict={}
    i=0
    #aasign a code to each letter
    for letter in ascii_lowercase:
        code_dict[letter]=codes[i]
        i+=1
    
    #assign a code to the spaces
    code_dict[" "]=codes[i]
    return code_dict


def encode_message(input_message, code_dict):
    # print(codes)
    encoded_message=''
    for element in input_message:
        encoded_message+=code_dict[element.lower()]
    return encoded_message
    
# print(encoded_message)

code_dict={}

input_option=''
while input_option != 'Q':
    print("""
(C)reate new encoding
(E)ncode message
(D)ecode message
(Q)uit
    """)

    input_option=input("Coose an option: ")
    if input_option == 'C':
        code_dict= create_code()
        print(code_dict)
    elif input_option == 'E':
        if code_dict == {}:
            print('No code was created yet')
        else:
            message=input('Intoduce your message: ')
            encoded_message = encode_message(message,code_dict)
            print(encoded_message)



