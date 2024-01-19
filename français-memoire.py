
# Modification date: Sun Jan 16 17:06:06 2022

# Production date: Sun Sep  3 15:43:43 2023

#imports
import csv
import random
import os


#functions
def get_dictionary(da_file):
	file = open(da_file)#'the_dictionary.csv'
	csvreader = csv.reader(file)
	rows = []
	for row in csvreader:
		rows.append(row)
	return rows
	
def get_all_words(the_dictionary):
	all_words = []
	for element in the_dictionary:
		if len(element) != 1:
			all_words.append(element)
	return all_words

def same_letter_words(letter, the_dictionary):
	in_the_range = False
	the_word_list = []
	for element in the_dictionary:
		if element[0].startswith("start of"):
			if element[0][-1] == letter:
				in_the_range = True
				continue
		elif element[0].startswith("end of"):
			in_the_range = False
			continue
		if in_the_range:
			the_word_list.append(element)
	return the_word_list

def add_word(the_word_prop_list, the_dictionary):
	da_letter = the_word_prop_list[0][0]#get index of start of letter list.index("")
	da_index_word = [f"end of {da_letter}"]
	real_index = the_dictionary.index(da_index_word)
	the_dictionary.insert(real_index, the_word_prop_list)
	
	#print(the_dictionary)
	with open('the_dictionary.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		# write multiple rows
		writer.writerows(the_dictionary)
	all_words = get_all_words(the_dictionary)
	return the_dictionary, all_words
	
	
	"""
	header = ['name', 'area', 'country_code2', 'country_code3']
	data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
	]

	with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    	writer = csv.writer(f)

    	# write the header
    	writer.writerow(header)

    	# write multiple rows
    	writer.writerows(data)

	"""
	return
	
def remove_word(word, the_dictionary):
	found = False
	for i in range(len(the_dictionary)):
		if the_dictionary[i][0].startswith(word):
			print(f"removing {the_dictionary[i]}")
			the_dictionary.pop(i)
			found = True
			break
	if not found:
		word = input("Word not found. Please reenter the word: ")
		return remove_word(word, the_dictionary)

	
	#print(the_dictionary)
	with open('the_dictionary.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		# write multiple rows
		writer.writerows(the_dictionary)
	
	all_words = get_all_words(the_dictionary)
	return the_dictionary, all_words

def word_game(all_words, right_guesses = 0, wrong_guesses = 0, continue_playing = True):

	the_word = random.choice(all_words)
	theq = random.choice(["fr", "tr"])
	if theq == "fr":
		guess = input(f"To quit, enter \"quit\".\nScore: {right_guesses * 2 - wrong_guesses}, right answers: {right_guesses}, wrong answers: {wrong_guesses}\nWhat's the turkish translation of {the_word[0]}?\n: ")
        if guess == the_word[3]:
			print("Congrats! Your guess is right!")
            right_guesses += 1
        elif guess == quit:
            return
        else:
			print(f"The answer was {the_word[3]}")
            wrong_guesses += 1
		return
	else:
		guess = input(f"To quit, enter \"quit\".\nScore: {right_guesses * 2 - wrong_guesses}, right answers: {right_guesses}, wrong answers: {wrong_guesses}\nWhat's the french translation of {the_word[3]}?\n: ")
		if guess == the_word[0].split("(", 1)[0]:
			print("Congrats! Your guess is right!")
		else:
			print(f"The answer was {the_word[0]}")
		return
		

def main_menu():
	return

whole_dic = get_dictionary('the_dictionary.csv')
all_words = get_all_words(whole_dic)

#car_word = ["voiture(la)", "Un veichule de transport qui fait Vroooooommm.", "Un veichule de transport pour 2-8 personnes.", "araba", "4 tekerli araç(tofaş)", "4 tekerlekli genelde 4 kişi taşıyabilen bir ulaşım aracı."]
#the_dictionary = add_word(car_word, whole_dic)
#all_words = get_all_words(whole_dic)

#whole_dic = remove_word("voiture", whole_dic)

word_game(all_words)