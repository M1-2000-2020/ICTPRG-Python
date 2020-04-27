
wordsSentence = input('Please enter a sentence: ')
length = len(wordsSentence)
count = 0
counter = 0

while count < length:
    if wordsSentence[count] == 'a' or wordsSentence[count] == 'e' or wordsSentence[count] == 'i' or wordsSentence[count] == 'o' or wordsSentence[count] == 'u':
        counter += 1
    count += 1
print("Vowels in this sentence is: ", counter)
