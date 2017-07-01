# def stupid(num):
#     if num==10:
#         return
#     else:
#         print('our number is', num)
#         stupid(num+1)

#stupid(0)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

ans = factorial(12)
print(ans)
