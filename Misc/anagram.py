from collections import defaultdict

def is_anagram(source, dest):
    source = source.replace(" ","").lower()
    dest = dest.replace(" ","").lower()

    if(len(source) != len(dest)):
        return False

    
    char_dict = defaultdict(int)


    for char in source:
        char_dict[char] += 1


    for char in dest:
        if char_dict[char] <=0:
            return False
        else:
            char_dict[char] -=1

    
    for char in char_dict:
        if char_dict[char] >0:
            return False

    return True

print(is_anagram("clint eastwood", "old west action"))