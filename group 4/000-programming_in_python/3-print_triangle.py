def print_right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__=="__main__":
    print(print_right_triangle(height=5))