# Caesars Cypher

# create functions that shift letters in an alphabet by a given number.

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# string input to lower
sentence = input("Type a sentence to encode: ").lower()
# strip whitespace + join
stripSentenceSpaces = "".join(sentence.split())
# convert sentence to list
sentenceList = list(stripSentenceSpaces)
# input how many numbers to shift the sentence back
shift = int(input("Pick a number to scramble the code:"))

# necessary vars
code = []  # sentence converted to numbers
codeMinusShift = []  # sentence numbers shuffled
finalCode = []  # shuffled sentence numbers converted to alpha
cypher = ""  # final code in string form
decode = []
decoded = ""

# convert sentence to index numbers; add to list var (code)


def convert():
    for i in sentenceList:
        code.append(alpha.index(i))

# shift numbers back x; add to list codeMinusShift


def convert2(x):
    if sentence:
        for i in sentenceList:
            codeMinusShift.append(alpha.index(i) - x)


# convert shuffled letter list back to alpha; add to list finalCode; print cypher


def createCode():
    convert()  # convert sentence to numbers function
    convert2(shift)  # shift numbers back x function
    for i in codeMinusShift:
        finalCode.append(alpha[i])
    print(f"This is The Secret Code: {cypher.join(finalCode)}")


# RUN IT!
createCode()

# DECODE IT!
# Easy way; printing the original string.
# Harder way; decoding original numbered string to alpha
# To see the easy option, enter 0; harder option, enter 1

decodeCypher = int(
    input("Would you like to decode the cypher?: Type '0' for Yes or '1' for No: "))

# convert the code to alpha


def decoder():
    for i in code:
        decode.append(alpha[i])
    print(f"This is The Secret Code Decoded: {decoded.join(decode)}")


if decodeCypher == 0:  # easy way; original input
    print(f"Decoded:{sentence} ")
elif decodeCypher == 1:  # harder way; no whitespace line output
    decoder()
