sentence = input("give me anything!!!")
sentence=sentence.split(' ')
max=0
for i in range(len(sentence)):
		if max<=len(sentence[i]):
			max=len(sentence[i])
			thesi=i
print (sentence[thesi])	
a=input("VOILA!!!!!")		