# def func(arr):
#     n = len(arr)
#     arr1 = []
#     arr2 = []
#     for element in sorted(arr)[::-1]:
#         if sum(arr1)<=sum(arr2):
#             if len(arr1) < n//2:
#                 arr1.append(element)
#             else:
#                 arr2.append(element)
#         else:
#             if len(arr2) < n//2:
#                 arr2.append(element)
#             else:
#                 arr1.append(element)
#     print(arr1)
#     print(arr2)
#     print(abs(sum(arr1)-sum(arr2)))

# func([3,4,5,3,100,1,83,54,23,20])

# print(4+100+1+23+20)
# print(3+5+3+83+54)

def func(arr):
    s = sum(arr)
    n = len(arr)
    count1 = 0
    count2 = 0
    desired_sum_arr = s//2
    temp = desired_sum_arr
    arr1 = []
    arr2 = []
    for i in sorted(arr)[::-1]:
        if temp - i >= 0 and count1< n//2:
            arr1.append(i)
            temp -= i
            count1 += 1
        # else:
        #     if count2 < n//2:
        #         arr2.append(i)
        #         count2 += 1
        #     else:
        #         arr1.append(i)
        #         temp -= i
        #         count1 += 1
    print(arr1, arr2)
    print(s, desired_sum_arr, temp)
    return s-(desired_sum_arr-temp)*2

print(func([3,4,5,3,100,1,83,54,23,20]))