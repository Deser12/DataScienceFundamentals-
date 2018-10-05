sentence = input("Write down a sentence")

list_words = sentence.split(" ")

numberof_listwords = len(list_words)

number1 = round(numberof_listwords * 0.25)
number2 = round(numberof_listwords * 0.75)

slice_sentence = list_words[number1:number2]

glue = " "
new_sentence = glue.join(slice_sentence)

print(new_sentence)
