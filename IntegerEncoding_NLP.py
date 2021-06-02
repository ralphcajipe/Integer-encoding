# Integer Encoding in NLP

vocab = {}  
word_encoding = 1 # start at index 1
def one_hot_encoding(text):
  global word_encoding

  words = text.lower().split(" ") 
  encoding = []  

  for word in words:
    if word in vocab:
      code = vocab[word]  
      encoding.append(code) 
    else:
      vocab[word] = word_encoding
      encoding.append(word_encoding)
      word_encoding += 1
  
  return encoding

text = "This is a test to see if this test will work. This is test one"
encoding = one_hot_encoding(text)
print("Integer encoding on maintained order:")
print(encoding)
print("\nVocabulary and their index number:")
print(vocab)

'''
OUTPUT:
Integer encoding on maintained order:
[1, 2, 3, 4, 5, 6, 7, 1, 4, 8, 9, 1, 2, 4, 10]

Vocabulary and their index number:
{'this': 1, 'is': 2, 'a': 3, 'test': 4, 'to': 5, 'see': 6, 'if': 7, 'will': 8, 'work.': 9, 'one': 10}

******************************************************************************************************
And now let's have a look at one hot encoding on our movie reviews:

positive_review = "I thought the movie was going to be bad but it was actually amazing"
negative_review = "I thought the movie was going to be amazing but it was actually bad"

pos_encode = one_hot_encoding(positive_review)
neg_encode = one_hot_encoding(negative_review)

print("Positive:", pos_encode)
print("Negative:", neg_encode)

OUTPUT:
Positive: [11, 12, 13, 14, 15, 16, 5, 17, 18, 19, 20, 15, 21, 22]
Negative: [11, 12, 13, 14, 15, 16, 5, 17, 22, 19, 20, 15, 21, 18]

Much better, now we are keeping track of the order of words and we can tell where each occurs.
'''