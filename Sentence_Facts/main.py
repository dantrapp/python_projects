

sentence = input("Type a sentence and we'll spit out some facts!: ").split()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

counter = 0
letter_count = 0
word_count = 0
longest_word = ""
most_used_letter = ""
letter_list = []

'''
count the words: DONE
count the number of letters: DONE
find the longest word: DONE

find the most used letter
  - create an alpha list. 
  - loop through alpha list: If l == "a", most_used_letter = l 
  loop through a-z
  loop through list of letters, i.e. letter_list.
  for i in alpha:
    if i.count(letter_list) < alpha_count:
      alpha_count += int(i)

  use this resource as an example
  https://www.geeksforgeeks.org/python-count-occurrences-element-list/
'''

#all outside vars must be set to global to be used in functions.

# The below isn't working, but I feel like I'm getting somewhere with the logic.

# def alphalist(x):
#   global alpha
#   global most_used_letter
#   for a in alpha[0, len(alpha)]:
#     for i in x:
#       if a == i:
#         most_used_letter = i




#function 
def facts(x):
  global counter 
  global word_count
  global longest_word
  global letter_count
  global most_used_letter
  global letter_list
  for i in x:
    counter += 1 #increment the counter
    letter_count += len(i) #add number letters of each word to letter_count
    letter_list += i #add all of the letters to a list for use in occurrence
    if word_count < len(i): #if 0 is less than the current word.
      word_count = len(i) #...add the length of the word to word_count
      longest_word = i # then add the current word to longest_word, until the longest word can either be replaced, or no other word is longer.

  print(f"There are {counter} words and {letter_count} letters in your sentence.")

  print(f"The word {longest_word} has the highest number of letters at {word_count} letters. The letter with the highest number of instance is {most_used_letter}")

  print(letter_list)



facts(sentence)


