#Author:JTI 11/3/21
palindrome = (str(input("Please enter a palindrome: ")))
if (palindrome[::-1] == palindrome):
  print(palindrome + "is a palindrome")
else:
  print((palindrome + "is a not palindrome"))
