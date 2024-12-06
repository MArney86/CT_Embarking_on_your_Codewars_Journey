#Task 2 Even or Odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Task 2 Convert a Number into a string!

def number_to_string(num):
    return str(num)

#Task 3 Vowel Count

def get_count(sentence):
    vowel_repo = "aeiou"
    vowel_count = 0
    for character in sentence:
        if character in vowel_repo:
            vowel_count += 1
        else:
            continue
    return vowel_count