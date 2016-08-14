#-*-coding:utf8-*-
from nltk.corpus import wordnet

#for synset in wordnet.synsets('say'):print(synset.definition(),synset.examples())


from sqlite3 import connect
conn=connect('cwn_dirty.sqlite')
c=conn.cursor()

lemma_type='打'
c.execute('select * from cwn_lemma where lemma_type="'+lemma_type+'"')
cwn_lemma=c.fetchone()

