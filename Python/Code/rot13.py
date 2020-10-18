def rot13_encode(text):
    abcd = "abcdefghijklmnopqrstuvwxyz" 
    result = ""
    for i in text:
        old_pos = abcd.find(i)
        result += abcd[(old_pos + 13) % 26]
    return result

# print(rot13_encode("hello")) outputs uryyb
