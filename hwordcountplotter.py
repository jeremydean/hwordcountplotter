
# coding: utf-8

# In[14]:

# 1. Call the hypothesis API with max limit (200) 

# 2. Use "offset" to grab more than one set

# 3. Grab it all for the specified user

import json

baseurl = "https://hypothes.is/api/search?"
#user = "jeremydean"
limit = "200"

# search for all annotations with an input username and return them in json format.
user = input("What user do you want to search for in Hypothesis?").lower()


searchurl = baseurl + "user=" + user + "&limit=" + limit
print(searchurl)

import requests
l = requests.get(searchurl)
l = json.loads(l.text)

total = l["total"]
#print(total)

loops = total // int(limit) + 1

'''
for offset in range(loops):
    l = requests.get(searchurl + "&offset=" + str(offset * 200))
    l = json.loads(l.text)

    for note in l["rows"]:
        print(note["text"])
        break
'''
    
#print(l["rows"][0]["text"])


#MERGED


#Split data into comments and then words

'''
for entry in l:
    p = Annotation(entry)
    x = p.comment
#    print(x)
#    print(type(x))
    print(x.split(" "))
'''
    
#Tokenize

import json
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string

#print(len(l["rows"]))
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['...', '``', "''", "'s", "n't", "http", "https", "'d", '--', "'m"]

#print(stop)

count_all = Counter()

totalcount = 0

for offset in range(loops):
    l = requests.get(searchurl + "&offset=" + str(offset * 200))
    l = json.loads(l.text)

    for note in l["rows"]:
        totalcount += 1
        #print(note["text"])
        #break
        terms = []
        #print(note)
        #terms = [term.lower() for term in TweetTokenizer().tokenize(text) if term not in stop]
        for term in word_tokenize(note["text"]):
            if term.lower() not in stop:
                terms.append(term.lower())
        count_all.update(terms)
        
print(totalcount)
        
#Print the first 10 most frequent words
print(count_all.most_common(10))

#Plotting

get_ipython().magic('matplotlib inline')
count_all_dict = dict(count_all.most_common(10))
import matplotlib.pyplot as plt
#plt.figure(figsize=(100, 40))
plt.bar(range(len(count_all_dict)), count_all_dict.values(), align='center')
plt.xticks(range(len(count_all_dict)), list(count_all_dict.keys()),rotation='vertical')

plt.show()

