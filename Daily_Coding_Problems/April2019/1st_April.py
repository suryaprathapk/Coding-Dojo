#Encoding
def encode(s):
    if not s:
        return ''

    result = ''
    current_char = s[0]
    current_count = 1
    for i, char in enumerate(s, 1):
        if char == current_char:
            current_count += 1
        else:
            result += str(current_count) + current_char
            current_char = char
            current_count = 1
    result += str(current_count) + current_char
    return result

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