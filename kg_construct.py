import os
import sys
import pickle


ents = open('dataset_ents.txt','r').readlines()
articles = open('/afs/crc.nd.edu/group/dmsquare/vol1/data/EngGigV5/corpus/typed_enggigv5.txt','r').readlines()
print(len(articles))

dictionary = {}
kg = {}

for ent in ents:
	ent = ent.split(' ')[0]
	dictionary[ent] = ent

#print(dictionary)

indexes = open('filtered_news.txt','r').readlines()

count = 0

for index in indexes:
    count += 1
    index = int(index)
    if index - 1 >= len(articles):
        break
    if count % 10000 == 0:
        print(count)
    parent = ''
    child = ''
    pidx = 0
    cidx = 0
    article = articles[index-1].split()
    i = 0
    while i < len(article):
        token = article[i]
        if token[0] == '$' and ':' in token and token.split(':')[1] in dictionary:
            if parent == '':
                parent = token.split(':')[1]
                pidx = i
            else:
                child = token.split(':')[1]
                cidx = i
                #print(pidx,cidx)

                if parent not in kg:
                    kg[parent] = {}
                    #print(' '.join(article[pidx+1:cidx]))
                    kg[parent][child] = {}
                    if cidx - pidx <= 10 and ',' not in ' '.join(article[pidx+1:cidx]) and '.' not in ' '.join(article[pidx+1:cidx]) and '?' not in ' '.join(article[pidx+1:cidx]) and '!' not in ' '.join(article[pidx+1:cidx]):
                        if len(' '.join(article[pidx+1:cidx])) > 0 and ' '.join(article[pidx+1:cidx])[0] != ' '.join(article[pidx+1:cidx])[0].upper():
                            if ' '.join(article[pidx+1:cidx]) in kg[parent][child]:
                                kg[parent][child][' '.join(article[pidx+1:cidx])] += 1
                            else:
                                kg[parent][child][' '.join(article[pidx+1:cidx])] = 1
                else:
                    if child not in kg[parent]:
                        kg[parent][child] = {}
                    #print(' '.join(article[pidx+1:cidx]))
                    if cidx - pidx <= 10 and ',' not in ' '.join(article[pidx+1:cidx]) and '.' not in ' '.join(article[pidx+1:cidx]) and '?' not in ' '.join(article[pidx+1:cidx]) and '!' not in ' '.join(article[pidx+1:cidx]):
                        if len(' '.join(article[pidx+1:cidx])) > 0 and ' '.join(article[pidx+1:cidx])[0] != ' '.join(article[pidx+1:cidx])[0].upper():
                            if ' '.join(article[pidx+1:cidx]) in kg[parent][child]:
                                kg[parent][child][' '.join(article[pidx+1:cidx])] += 1
                            else:
                                kg[parent][child][' '.join(article[pidx+1:cidx])] = 1
                    
                parent = ''
                child = ''
                pidx = 0
                cidx = 0
                i -= 1
        i += 1
with open('/afs/crc.nd.edu/group/dmsquare/vol1/data/EngGigV5/corpus/kg_whole.pickle','wb') as handle:
    pickle.dump(kg,handle,protocol=pickle.HIGHEST_PROTOCOL)

'''
for article in articles:
	count += 1
	if count % 10000 == 0:
		print(count)
	tokens = article.split()
	parent = ''
	child = ''
	pidx = 0
	cidx = 0
	for i,token in enumerate(tokens):
		if token in dictionary:
			if parent == '':
				parent = token
				pidx = i
			else:
				child = token
				cidx = i
				#print(parent,child)
				if parent not in kg:
					kg[parent] = {}
					kg[parent][child] = [tokens[pidx+1:cidx]]
				else:
					if child not in kg[parent]:
						kg[parent][child] = []
					kg[parent][child].append(tokens[pidx+1:cidx])
				parent = ''
				child = ''
				pidx = 0
				cidx = 0
'''

