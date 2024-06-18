def get_smallest_integer(my_list):
    if not my_list:  
        return None
    smallest = my_list[0]
    for num in my_list:
        if num < smallest:
            smallest = num
    return smallest
if __name__=="__main__":
    print(get_smallest_integer(my_list=[7,9,4,99]))