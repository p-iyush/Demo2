def func(larger_string, smaller_string):
    ans = []
    s = larger_string.split()
    for i in s:
        if i != smaller_string:
            ans.append(i)
    print(*ans)

func(input(), input())

# func("My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush My nams is Piyush ", "is")
            