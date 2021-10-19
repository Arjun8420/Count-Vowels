#Program to count the number of Vowels in a String

String = input("Enter the String to check for Vowels = ")

vowels = "aeiou"
vCount = 0

for c in vowels:
    if c in vowels:
        vCount +=1

print("Number of vowels = ",vCount)
