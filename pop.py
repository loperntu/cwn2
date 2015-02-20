from __future__ import division
from numpy import dot
from math import sqrt
def lesk(example,kwic):
    return len([w for w in example if w in kwic])/min(len(example),len(kwic))
def cos_similar(v1,v2):
    len1=sum([i**2 for i in v1])
    len2=sum([i**2 for i in v2])
    d=dot(v1,v2)
    if d>0:return d/sqrt(len1)/sqrt(len2)
    return 0

plurks=[plurk.strip() for plurk in open('asbc.txt')]

d=dict() # {lemma:{definition:[lesk]}}
for line in open('CWNMOE-def-ex.csv'):
    lemma,definition,example=line.split(',')
    lemma,definition,example=lemma.strip('"'),definition.strip('"').strip(),example.strip().strip('"').strip()
    example_words=example.split()
    flag=1
    for plurk in plurks:
        plurk_words=plurk.split()
        if lemma in plurk_words: # concordanced context
            lesk_score=lesk(example_words,plurk_words)
            if lemma not in d:d[lemma]={definition:[lesk_score]}
            elif definition not in d[lemma]:d[lemma][definition]=[lesk_score]
            else:d[lemma][definition].append(lesk_score)
            flag=0
    if flag:d[lemma]={definition:[0]}

for lemma in d:
    i=0
    while i<len(d[lemma].keys()):
        j=0
        while j<i and j<len(d[lemma].keys()) and i<len(d[lemma].keys()):
            def1,def2=d[lemma].keys()[i],d[lemma].keys()[j]
            v1,v2=d[lemma][def1],d[lemma][def2]
            if len(v1)==len(v2):
                if cos_similar(v1,v2)>.2:
                    d[lemma].pop(def1)
                    if i<len(d[lemma].keys()):continue
                else:j+=1
            else:j+=1
        i+=1

for lemma in d:
    for definition in d[lemma]:print lemma,definition
