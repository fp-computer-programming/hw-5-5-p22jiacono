#Author:JTI 11/3/21

input_string = input("Enter text: ")
splice = int(len(input_string) / 2)
print(input_string[:splice])
print(input_string[splice:])
