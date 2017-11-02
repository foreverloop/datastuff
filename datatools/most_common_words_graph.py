#most_common_words_graph.py
import requests
from collections import Counter
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup

titles = list()
words = list()
word_numbers = list()

def get_title(span):
  titles.append(span.text)

html = requests.get("http://www.theguardian.com").text
soup = BeautifulSoup(html,'html5lib')
exclude_list = "is,in,on,the,for,and,of,a,to,-,v,from,at,says,has,be"

for span in soup('span','js-headline-text'):
  get_title(span)

counter = Counter(word.lower()
				  for line in titles
				  for word in line.strip().split()
				  if not word in exclude_list)

#need lists for the bar plot
for word,count in counter.most_common(10):
  words.append(word)
  word_numbers.append(count)

xs = [i + 0.1 for i, _ in enumerate(words)]

plt.bar(xs,word_numbers)
plt.ylabel("Word Frequency")
plt.title("Common Words in Guardian Headlines")
plt.xticks([i + 0.5 for i, _ in enumerate(words)],words)
plt.show()
