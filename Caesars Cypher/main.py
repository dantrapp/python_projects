# Caesars Cypher

# create functions that shift letters in an alphabet by a given number.

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sentence = input("Type a sentence to encode: ").lower()
stripSentenceSpaces = "".join(sentence.split())
sentenceList = list(stripSentenceSpaces)
shift = int(input("Pick a number to scramble the code:"))
code = []  # sentence converted to numbers
codeMinusShift = []  # sentence numbers shuffled
finalCode = []  # shuffled sentence numbers converted to alpha
cypher = ""  # final code in string form


# convert sentence to index numbers; add to list var (code)
def convert():
    for i in sentenceList:
        code.append(alpha.index(i))

# shift numbers back x


def convert2(x):
    for i in sentenceList:
        codeMinusShift.append(alpha.index(i) - x)

# convert shuffled letter list back to alpha and print the code.


def createCode():
    convert()  # convert sentence to numbers
    convert2(shift)  # shift numbers back x
    for i in codeMinusShift:
        finalCode.append(alpha[i])
    print(f"This is The Secret Code: {cypher.join(finalCode)}")


# RUN IT!
createCode()
