
import re 
import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords')


with open("words.txt") as file:
    text = file.read()


words = re.split(r'[ \n.,;!?\(\)\[\]\{\}\'\"]+', text)
words = words[:-1] 
print('Number of words Including stop words): ', len(words))
print('First 20 words:')
print(words[:20])
print('Last 20 words:')
print(words[-20:])



stop_words = stopwords.words('english')
print('Number of stop words: ', len(stop_words))
print('List of the current stop words: ')
print(stop_words)

filtered_words = [word for word in words if word.lower() not in stop_words]
print('Number of words after removing stop words: ', len(filtered_words))
print('First 20 words:')
print(filtered_words[0:20])
print('Last 20 words:')
print(filtered_words[-20:])


words_frequency = {}
for word in filtered_words:
    if word in words_frequency.keys():
        words_frequency[word]+=1
    else:
        words_frequency[word]=1
        
print('Number of unique words: ', len(words_frequency))

top_words = [word for word in words_frequency.keys() if words_frequency[word]>500]
print('Number of words occuring more than 500 times: ', len(top_words))
print('List of words occuring more than 500 times:')
print(top_words)
