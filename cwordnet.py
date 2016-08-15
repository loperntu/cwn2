#-*-coding:utf8-*-
from nltk.corpus import wordnet

#for synset in wordnet.synsets('say'):print(synset.definition(),synset.examples())


from sqlite3 import connect
conn=connect(database='/home/ubuntu/cwn_dirty.sqlite')
c=conn.cursor()

def lookup_lemma_ids(lemma_type='提醒'):
    lemma_ids=[]
    c.execute('select * from cwn_lemma where lemma_type="'+lemma_type+'"')
    for lemma_id,cwn_pinyin,cwn_zhuyin,lemma_sno,lemma_type,meet_date,mod_time,supersense in c.fetchall():
        lemma_ids.append(lemma_id)
        print(lemma_type)
    return lemma_ids

def lookup_sense_ids(lemma_id):
    sense_ids=[]
    c.execute('select * from cwn_sense where lemma_id="'+lemma_id+'"')
    for sense_id,lemma_id,sense_def,domain_id,sense_synonym,sense_antonym,sense_varword,sense_nearsyn,sense_relword,synset_id in c.fetchall():
        sense_ids.append(sense_id)
        print(sense_def)
    return sense_ids

def lookup_example_conts(sense_id):
    example_conts=[]
    c.execute('select * from cwn_example where cwn_id="'+sense_id+'"')
    for cwn_id,example_sno,example_cont in c.fetchall():
        example_conts.append(example_cont)
        print(example_cont)
    return example_conts

print('lemma_types:')
for lemma_id in lookup_lemma_ids(lemma_type='管理'):
    print('sense_defs:')
    for sense_id in lookup_sense_ids(lemma_id):
        print('example_conts:')
        for example_cont in lookup_example_conts(sense_id):
            pass
