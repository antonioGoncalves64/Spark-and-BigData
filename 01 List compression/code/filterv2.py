sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'

def is_consonant(letter):
	vowels = 'aeiou'
	return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]

print("consantes= ",consonants)