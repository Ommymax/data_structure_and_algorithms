def find_first_occurrence(my_list, num):
    for index, value in enumerate(my_list):
        if value == num:
            return index
    return -1 
if __name__=="__main__":
    print(find_first_occurrence(my_list=[7,7,9,4,99],num=7))