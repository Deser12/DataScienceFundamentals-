wrong_words = ["worsd", "wlong", "si", "plogram", "displai"]

good_words = ["words", "wrong", "is", "program", "display"]

input_words = input("Write down a sentence")

check_words = input_words.split(" ")

index = 0 

for word in check_words: 

# if check_words in wrong_words
	if word in wrong_words:
		index = wrong_words.index(word)
		check = good_words[index]
		print("Hmm, " + word + " is spelled wrong! I think you mean " + check)
		 
index += 1
