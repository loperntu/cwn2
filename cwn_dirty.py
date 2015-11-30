#-*-coding:utf8-*-
from sqlite3 import connect


def lookup_lemma_id(lemma_type):
    conn=connect('../cwn_dirty.sqlite')
    c=conn.cursor()
    c.execute('select * from cwn_lemma where lemma_type="'+lemma_type+'"')
    cwn_lemma=c.fetchone()
    lemma_id,cwn_pinyin,cwn_zhuyin,lemma_sno,lemma_type,meet_date,mod_time,supersense=cwn_lemma
    conn.close()
    return lemma_id

def lookup_senses(lemma_type):
#    conn=connect('../cwn_dirty.sqlite')
 #   c=conn.cursor()
    lemma_id=lookup_lemma_id(lemma_type)
    c.execute('select * from cwn_sense where lemma_id="'+lemma_id+'"')
    cwn_senses=c.fetchall()
    d={'senses':[]}
    for cwn_sense in cwn_senses:
#        d['senses'].append(cwn_sense[2])
        print lemma_type.encode('utf8'),cwn_sense[2].encode('utf8')
  #  conn.close()
    return d

def lookup_relation(cwn_lemma):
    rel_lemmas=[]
    conn=connect('../cwn_dirty.sqlite')
    c=conn.cursor()
    c.execute('select * from cwn_relation where cwn_lemma="%s"' % cwn_lemma)
    for cwn_relation in c.fetchall():
        relation_id,cwn_id,rel_sno,rel_type,rel_lemma,rel_refid,rel_cluster,rel_cwnid,rel_facet,cwn_lemma=cwn_relation
        rel_lemmas.append(rel_lemma)
    return rel_lemmas

conn=connect('../cwn_dirty.sqlite')
c=conn.cursor()
c.execute('select * from cwn_lemma')
cwn_lemmas=c.fetchall()
for cwn_lemma in cwn_lemmas:
    lemma_id,cwn_pinyin,cwn_zhuyin,lemma_sno,lemma_type,meet_date,mod_time,supersense=cwn_lemma
    lookup_senses(lemma_type)
conn.close()

#print lookup_lemma_id(u'高興')
#print lookup_lemma_id(u'快樂')
#print ' '.join(lookup_relation(u'阻'))
