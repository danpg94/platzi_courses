def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

result, width, text = find_volume(length=32)
print(result)
print(width)
print(text)