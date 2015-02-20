#-*-coding:utf8-*-
from sys import argv
from sqlite3 import connect
conn=connect('../cwn_dirty.sqlite')
c=conn.cursor()

def lookup_pos(lemma_id):
    c.execute('select * from cwn_pos where cwn_id like "%'+lemma_id+'%"')
    cwn_pos=c.fetchone()
    pos=cwn_pos[2]
    return pos

def lookup_sense(lemma_id):
    c.execute('select * from cwn_sense where lemma_id="'+lemma_id+'"')
    cwn_sense=c.fetchone()
    sense_def=cwn_sense[2]
    return sense_def

def lookup_lemma(lemma_id):
    c.execute('select * from cwn_lemma where lemma_id="'+lemma_id[:6]+'"')
    cwn_lemma=c.fetchone()
    lemma_type=cwn_lemma[4]
    return lemma_type

def lookup_lemma_ids(lemma_type):
    res=[]
    c.execute('select * from cwn_lemma where lemma_type="'+lemma_type+'"')
    for cwn_lemma in c.fetchall():
        lemma_id=cwn_lemma[0]
        res.append(lemma_id)
    return res

def add_to_dict(k,v,d):
    if k not in d:d[k]=[v]
    else:d[k].append(v)
    return d

def lookup_relations(lemma_id):
    res={}
    c.execute('select * from cwn_relation where cwn_id like "%'+lemma_id+'%"')
    for cwn_relation in c.fetchall():
        rel_type=cwn_relation[3]
        rel_lemma=cwn_relation[4]
        res=add_to_dict(rel_type,rel_lemma,res)
    return res

class synset:
    def __init__(self,lemma_type):
        self.lemma_type=lemma_type
        self.synonyms=[]
        self.antonyms=[]
        self.hyponyms=[]
        self.hypernyms=[]
        for lemma_id in lookup_lemma_ids(lemma_type):
            for rel_type,rel_lemmas in lookup_relations(lemma_id).items():
                if rel_type=='=':
                    for rel_lemma in rel_lemmas:self.add_synonym(rel_lemma)
                elif rel_type=='!':
                    for rel_lemma in rel_lemmas:self.add_antonym(rel_lemma)
                elif rel_type=='~':
                    for rel_lemma in rel_lemmas:self.add_hyponym(rel_lemma)
                elif rel_type=='@':
                    for rel_lemma in rel_lemmas:self.add_hypernym(rel_lemma)
    def add_synonym(self,synonym):
        self.synonyms.append(synonym)
    def add_antonym(self,antonym):
        self.antonyms.append(antonym)
    def add_hyponym(self,hyponym):
        self.hyponyms.append(hyponym)
    def add_hypernym(self,hypernym):
        self.hypernyms.append(hypernym)
        

s=synset(argv[1])
print 'synonyms:',' '.join(s.synonyms)
print 'antonyms:',' '.join(s.antonyms)
print 'hyponyms:',' '.join(s.hyponyms)
print 'hypernyms:',' '.join(s.hypernyms)
