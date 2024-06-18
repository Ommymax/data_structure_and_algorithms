def character_frequency(string):
    frequency = {}
    for char in string.lower():
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency
if __name__=="__main__":
    print(character_frequency(string='mama'))
