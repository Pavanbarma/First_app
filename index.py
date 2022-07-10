# n = int(input())
# if n >= 0:
#     if (n >= 30) and (n <= 50):
#         print("Average")
#     elif (n >= 51) and (n <= 60):
#         print("Good")
#     elif (n >= 61) and (n <= 80):
#         print("Excellent")
#     else:
#         print("Outstanding")
# else:
#     print("Number should be graterthan Zero")
    
    
n = int(input())
a = list(map(int, input().split()))
new = []
for i in a:
    if i > 0:
        new.append(a.index(i))
print(len(new))