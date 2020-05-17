#ANAGRAMS


def read_letters(letters, letterset):
    list_input = letters.split(",")
    for i in range(0,len(list_input)):
        letterset.add(list_input[i])
    return letterset

def open_dictionary(dictName):
    dict_list = []
    with open(dictName, "r") as f:
        for line in f:
            for word in line.split():
                word = word.lower()
                dict_list.append(word)
    dict_set = set()
    for i in range(0, len(dict_list)):
        dict_set.add(dict_list[i])
    return dict_set

def permute(word, l, length, perm_list):
    #problem with perm_list
    if(l== length):
        perm_list.append(''.join(word))
    else:
        for i in range(l, length):
            word[l], word[i] = word[i], word[l]
            permute(word, l+1, length, perm_list)
            word[l], word[i] = word[i], word[l]
    return perm_list

def remove_duplicates(perm_list):
    new_list = []
    for word in perm_list:
        if word not in new_list:
            new_list.append(word)
    return new_list

def checkingwords(word, dict_set, officialWords):
    if word in dict_set:
        return word
    else:
        return ""

def calc_score(word_length):
    switcher = {
        3: 30,
        4: 40,
        5: 50,
        6: 60,
        7: 70,
        8: 80,
        9: 90,
        10: 100,
        }
    return switcher.get(word_length, 0)

def check_panagram(word_split, letterset):
    addition_points = 0
    set_copy = letterset.copy()
    for letter in word_split:
        if(letter in set_copy):
            set_copy.remove(letter)
    if(len(set_copy) == 0):
        addition_points =  100
        print('Panagram! Nice!')
    return addition_points


def printList(user_words):
    print("-------------------------------")
    print("Your words:")
    for i in range(0,len(user_words)):
        print (user_words[i])
