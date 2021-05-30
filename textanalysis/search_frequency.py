import requests 
from bs4 import BeautifulSoup 
import operator 
import pandas as pd
from collections import Counter 
def start(url): 
	wordlist = [] 
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, 'html.parser')
	for each_text in soup.findAll():
		content = each_text.text
		words = content.lower().split() 
		for each_word in words:
			wordlist.append(each_word) 

		clean_list=[]
		for word in wordlist:
			symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
			for i in range (0, len(symbols)):
				word = word.replace(symbols[i], '')
			if len(word) > 0:
				clean_list.append(word)
		clean_commonlist=[]
		common_words_df = pd.read_csv('list.txt', names=['words'])
		common_wordslist = common_words_df['words'].values.tolist()
		clean_commonlist = [word for word in clean_list if word not in common_wordslist]
		word_count = {}
		for word in clean_commonlist:
			if word in word_count:
				word_count[word] += 1
			else:
				word_count[word] = 1
		c = Counter(word_count)
		top = c.most_common(15)
		return top, content

def analyze(djtext,removepunc, fullcaps, newline, spaceremove, charcount):
	global params
	analyzed = ''
    # Remove the listed 14 punctuations
    
	if removepunc == 'on':
		punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
		for i in djtext:
			if i not in punctuations:
				analyzed = analyzed+i
		params = {'purpose':'Remove punctuations','analyzed_text':analyzed}
    
	# Capitalize the entire text
    
	if fullcaps == 'on':
		djtext_lower= ''.join(djtext)
		if analyzed == '':
			analyzed = djtext_lower.upper()
		else:
			analyzed = analyzed.upper()
		params = {'purpose': 'Convert to upper case', 'analyzed_text': analyzed}
    
	# Remove all the newlines from the text
    
	if newline == 'on':
		if analyzed == '':
			for i in djtext:
				if i != "\n" and i != '\r':
					analyzed += i
		else:
			p = ''
			for i in analyzed:
				if i != "\n" and i != '\r':
					p += i
			analyzed = p
		params = {'purpose': 'Remove the new line', 'analyzed_text': analyzed}
    
	# Remove all the spaces from the text
    
	if spaceremove == 'on':
		if analyzed == '':
			for i in djtext:
				if i != ' ':
					analyzed += i
		else:
			p = ''
			for i in analyzed:
				if i != ' ':
					p += i
			analyzed = p
		params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
    
	# Count all the characters in the entered text
    
	if charcount == 'on':
		count = len(djtext)
		analyzed += str(count)
		params = {'purpose': 'Count the characters', 'analyzed_text': analyzed}
	return params