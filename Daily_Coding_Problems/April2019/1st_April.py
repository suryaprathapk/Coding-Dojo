#####Question#####

# April1, 2019
# This is your coding interview problem for today.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.


#######################




#Encoding
def encode(s):
    if not s:
        return ''

    result = ''
    current_char = s[0]
    current_count = 0
    for i, char in enumerate(s, 1):
        if char == current_char:
            current_count += 1
        else:
            result += str(current_count) + current_char
            current_char = char
            current_count = 1
    result += str(current_count) + current_char
    return result

print(encode("aaaabbbccd"))

#Decoding
def decode(s):
    count = 0
    result = ''
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            # char is alphabetic
            result += char * count
            count = 0
    return result