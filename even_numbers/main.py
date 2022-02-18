#fun with range()


for n in range(1, 10):
  print(n)

for n in range(1, 10, 2): #print by 2's using the [step] in range
  print(n)

#Even Numbers
'''
user inputs a number. Using a for loop and range, find all of the even numbers up to the number user inputted.

Count how many even numbers there are and add all even numbers to a dedicated list.
'''
num = int(input("Enter a number and we'll find all of the even numbers within the range: "))

even = (n % 2 == 0)
count = 0 #could change this to =len(even_list) for the same result.
even_list = []

for n in range(1, num+1):
  even = (n % 2 == 0)
  if even:
    even_list.append(n) #add even number to even_list
    count = count + 1 #increment counter (can also simply use len(even_list).
    print(n, "is even")
  #else: #comment out if you don't want to print odd numbers, too.
    #print(n, "is odd")

print(f"There are {count} even numbers between 1 and {num}")
print(f"Now we have a seperate list of even numbers {even_list}")
#print(len(even_list)) #uncomment if you'd rather use this instead of count var