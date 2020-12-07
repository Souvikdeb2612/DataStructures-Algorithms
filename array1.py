
#Reversing a string

def reverse(string):
  arr =[]
  for i in range(len(string)-1, -1, -1):
    arr.append(string[i])
  return "".join(arr)


print(reverse(string = input("input:")))



