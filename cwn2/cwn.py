#-*-coding:utf8-*-
from sys import argv
from sqlite3 import connect

class synset:
    def __init__(self,lemma_type):
        conn=connect('cwn_dirty.sqlite')
        self.c=conn.cursor()
        self.lemma_type=lemma_type
        self.synonyms=[]
        self.antonyms=[]
        self.hyponyms=[]
        self.hypernyms=[]
        for lemma_id in self.lookup_lemma_ids(lemma_type):
            for rel_type,rel_lemmas in self.lookup_relations(lemma_id).items():
                if rel_type=='=':
                    for rel_lemma in rel_lemmas:self.synonyms.append(rel_lemma)
                elif rel_type=='!':
                    for rel_lemma in rel_lemmas:self.antonyms.append(rel_lemma)
                elif rel_type=='~':
                    for rel_lemma in rel_lemmas:self.hyponyms.append(rel_lemma)
                elif rel_type=='@':
                    for rel_lemma in rel_lemmas:self.hypernyms.append(rel_lemma)

    def lookup_lemma_ids(self,lemma_type):
        res=[]
        self.c.execute('select * from cwn_lemma where lemma_type="'+lemma_type+'"')
        for cwn_lemma in self.c.fetchall():
            lemma_id=cwn_lemma[0]
            res.append(lemma_id)
        return res

    def add_to_dict(self,k,v,d):
        if k not in d:d[k]=[v]
        else:d[k].append(v)
        return d

    def lookup_relations(self,lemma_id):
        res={}
        self.c.execute('select * from cwn_relation where cwn_id like "%'+lemma_id+'%"')
        for cwn_relation in self.c.fetchall():
            rel_type=cwn_relation[3]
            rel_lemma=cwn_relation[4]
            res=self.add_to_dict(rel_type,rel_lemma,res)
        return res

if __name__=='__main__':
    s=synset(argv[1])
    print 'synonyms:',' '.join(s.synonyms)
    print 'antonyms:',' '.join(s.antonyms)
    print 'hyponyms:',' '.join(s.hyponyms)
    print 'hypernyms:',' '.join(s.hypernyms)
