# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]
another_word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.


def all_odd(number_list):

    all_odds = filter((lambda x : x%2 !=0), number_list)

    return all_odds

print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):

    all_evens = filter((lambda x : x % 2 == 0), number_list)

    return all_evens

print all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.

def long_words(word_list):


    filter(lambda x: len(x)>=4, word_list)

    return word_list

print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.

def smallest(number_list):

    x = min(number_list)

    return x

print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):

    x = max(number_list)

    return x

print largest(number_list)
# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def half(number_list):
    return number_list/2.0

def halvesies(number_list):
    
    numbers=map(half, number_list) #try not to define functions within functions unless you need to

    return numbers

print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    

    words=map(len, word_list) # for map, you just pass a function name in first argument, don't pass anything else. or else gnarly error. 

    return words
     
print "These are the results"
print word_lengths(another_word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    

    count=reduce(lambda x,y: x+y, number_list)

    return count

print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    
    count = reduce(lambda x,y: x*y, number_list)
    return count

print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    
    joined = reduce(lambda x,y: x+(' '+y), word_list)

    return joined

print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):

    count = reduce(lambda x,y: x+y, number_list)

    mean = float(count)/len(number_list)

    return mean

print average(number_list)