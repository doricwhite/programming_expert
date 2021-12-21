# -------------- Programming Expert: Introduction Assessments

# Question 1: Random Number Generator
import random

# Random Number Function
def random_number (start_num, end_num):
    number = random.randint(start_num, end_num)
    return number


# Guess number
def guess_number():
    while True:
        guess = input("Guess a number: ")

        try:
            guess = int(guess)
            break
        except ValueError:
            print("Please enter a valid number.")
    
    return guess


# Random Range
def random_range():
    entry = ["start", "end"]
    nums = []

    for x in range(len(entry)):
        while True:
            number = input(f"Enter the {entry[x]} of the range: ")

            try:
                number = int(number)
                if entry[x] == "end" and nums[0] > number:
                    print("Please enter a valid number.")
                    continue
                else:
                    break
                break
            except ValueError:
                print("Please enter a valid number.")
        
        
        # add number to list
        nums.append(number)

  
    return random_number(nums[0],nums[1])
        


random_result = random_range()
guessed_number = guess_number() 
count = 1

while random_result != guessed_number:
    guessed_number = guess_number()
    count += 1  

if count == 1:
    print (f"You guessed the number in {count} attempt")

else:
    print(f"You guessed the number in {count} attempts")



# Question 2: Caesar Cipher
def caesar_cipher(string, offset):
    cipher = ""

    for x in range(len(string)):
        letter = string[x]
        # Lower case letters offset to the left
        cipher += chr((ord(letter) - offset - 97) % 26 + 97)

    return cipher


# Question #3: Sort Employees
def sort_employees(employees, sort_by):
    # Write your code here.
    sort_choice = ["name", "age", "salary"]
    sorted_employees = employees
    idx = 0

    for x in range(len(sort_choice)):
        if sort_choice[x] == sort_by:
            idx = x

    def sort_index(lst):
        return lst[idx]
    
    sorted_employees.sort(key=sort_index)
    
    return sorted_employees


#Question 4: Longest Unique Words
def get_n_longest_unique_words(words, n):
    result = []
    char_count = []
    top_words=[]
    
    # Obtains unique words in list
    for word in words:
        if words.count(word) == 1:
            result.append(word)
    
    # Word count
    for x in range(len(result)):
        inner_word = result[x]
        char_count.append(len(inner_word))


    for y in range(n):
        max_char = max(char_count)
        top_words.append(result[char_count.index(max_char)])
        char_count[char_count.index(max_char)] = 0   


#Question 5: Pair Sum To Target
def pairs_sum_to_target(list1, list2, target):
    # Write your code here.
    total_index = []
    for x in range(len(list1)):
        for y in range(len(list2)):
            total = list1[x] + list2[y]
            if total == target:
                total_index.append([x,y])

    return total_index



# Question 6: Create String From Characters
def create_strings_from_characters(frequencies, string1, string2):
    # Write your code here.
    first_word = word_check(frequencies, string1)
    second_word = word_check(frequencies, string2)
    word_combined = string1 + string2
        
    if (not first_word) or (not second_word):
        if first_word or second_word:
            return 1
        
        return 0
    
    for char in word_combined:
        if char not in frequencies or frequencies[char] == 0:
            return 1

        frequencies[char] -= 1
    
    return 2

# Check for string letters available in the dictionary
def word_check (freq, word):
    for char in set(word):
       if word.count(char) > freq.get(char, 0):
           return False
    
    return True