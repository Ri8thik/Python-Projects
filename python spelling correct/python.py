from textblob import TextBlob
a=input("enter here:-- ")
print("original text:"+str(a))

b=TextBlob(a)
print("corrected text:"+str(b.correct()))
