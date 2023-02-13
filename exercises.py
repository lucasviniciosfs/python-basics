def repeat(text, repetitions):
    finalText = ''
    while repetitions > 0:
        finalText += text
        repetitions -= 1
    return finalText


print(repeat('*', 3))  # '***' 
print(repeat('abc', 2))  # 'abcabc' 
print(repeat('abc', 0))  # ''