def two_indices(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index
if __name__=="__main__":
   print(two_indices(nums=[2, 7, 11, 15],target= 9))
   
