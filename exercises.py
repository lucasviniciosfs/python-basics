def titleize(text):
    textStr = ''.join(text)
    words = textStr.split(' ')
    for word in words:
        words[words.index(word)] = word.replace(word[0], word[0].upper())
    return ' '.join(words)

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt')) 