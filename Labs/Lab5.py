def letter_vowel_cons_count(word):

	total_letter = 0
	total_vowel = 0
	total_cons = 0
	vowel = "AEIOUaeiou"
	
	for char in word:
		if char.isalpha():
			total_letter += 1
			if char in vowel:
				total_vowel += 1
			else:
				total_cons += 1
	return total_letter, total_vowel, total_cons
try:
	word = input("Enter a word!: ")
	total_letter, total_vowel, total_cons = letter_vowel_cons_count(word)
	print(f'Number of Letters is  {total_letter}, the number of Vowels is {total_vowel} and the number of Consonents is {total_cons}')
except:
	print("Hmmm, something went wrong. Try again. :(")
