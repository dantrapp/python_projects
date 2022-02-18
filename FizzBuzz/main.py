'''
FIZZBUZZ
The classic programmer job interview challenge.
Count to 100
Every number divisible by 3, say "Fizz"
Every number divisible by 5, say "Buzz"
Every number divisible by 3 & 5, say "FizzBuzz"
'''

fizz = 0
buzz = 0
fizzbuzz = 0

for n in range(1, 101):
  if n % 3 == 0:
    fizz += 1
    print("Fizz!")
  if n % 5 == 0 and n % 3 != 0:
    buzz += 1
    print("Buzz!")
  if n % 3 == 0 and n % 5 == 0:
    fizzbuzz += 1
    print("FizzBuzz!")
  else:
    print(f"{n}")

print(f"There are {fizz} instances of Fizz \n{buzz} instances of Buzz\nand {fizzbuzz} instances of FizzBuzz in the number 100 ")

  