KEYS = ['00100010011011010011100100101101', '11000111100111100111101100000111', '11011000001111101100001010001000', '11011111000111110011010010000101']

def string_to_binary(msg):
    ascii = [ord(x) for x in msg]
    binary_data = ''.join(format(byte, '08b') for byte in ascii) 
    return binary_data

def binary_to_string(binary_string):
    chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_characters = [chr(int(chunk, 2)) for chunk in chunks]
    ascii_string = ''.join(ascii_characters)
    
    return ascii_string

def xor(left, right):
    result = ''
    for i in range(len(left)):
        if left[i] == right[i]:
            result += '0'
        else:
            result += '1'
    return result

def cipher(message, keys=KEYS, rounds=4):
    binary_message = string_to_binary(message)
    n = len(binary_message) // 2
    left, right = binary_message[:n], binary_message[n:]

    for i in range(rounds):
        f = xor(right, keys[i])
        left, right = right, xor(left, f)

    left, right = right, left
    cipher_text = left + right
    return binary_to_string(cipher_text)

def decipher(message, keys=KEYS, rounds=4):
    binary_message = string_to_binary(message)
    n = len(binary_message) // 2
    left, right = binary_message[:n], binary_message[n:]

    keys = keys[::-1]

    for i in range(rounds):
        f = xor(right, keys[i])
        left, right = right, xor(left, f)
    
    left, right = right, left
    deciphered_text = left + right
    return binary_to_string(deciphered_text)
