x=input("enter the string -- ")
characterCount=0
wordCount=1
for i in x :
   characterCount = characterCount+1
   if(i==' '):
       wordCount = wordCount+1  
print("number of words in the string  -> ")
print(wordCount)
print("number of characters in the string  -> ")
print(characterCount)