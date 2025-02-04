class VowelCounter:
	def __init__(self):
		self.string=""
	def setString(self,input_string):
		self.string=input_string
	def countVowels(self):
		count=0
		for i in self.string:
			if i.lower() in "aeiou":
				count+=1
		return count
		

# Sample Input
input_string = input()

# Creating an instance of the VowelCounter class
counter = VowelCounter()

# Setting the input string
counter.setString(input_string)

# Counting the vowels in the string
result = counter.countVowels()
print(result)  # Output for the given sample input
