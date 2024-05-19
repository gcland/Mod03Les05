import re

with open("travel_blogs.txt", "r") as file:
    lines = file.readlines()

i=0
p=0
positive_list = ['enjoy', 'amazing', 'wonderful', "excellent", "fantastic", "beautiful", 'memorable' ,'enlightening']
pos_results = []
for line in lines:
    i+=1
    for positive_word in positive_list:
        if positive_word in line:
            print(f"Positive word: {positive_word} found!")
            match=re.search(positive_word, line)
            print(f"Start and end index of {positive_word.upper()}, line {i}, {match.span()}")
            pos_results.append(positive_word)
            p+=1
print(f"Positive word count: {p}.")
print()
negative_list = ['disappointing', 'poor', 'lackluster', 'bad']
neg_results = []
i=0
n=0
for line in lines:
    i+=1
    for negative_word in negative_list:
        if negative_word in line:
            print(f"Negative word: {negative_word} found.")
            match=re.search(negative_word, line)
            print(f"Start and end index of {negative_word.upper()}, line {i}, {match.span()}")
            neg_results.append(negative_word)
            n+=1
print(f"Negative word count: {n}.")