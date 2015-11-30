from sqlite3 import connect
conn=connect('cwn_dirty.sqlite')
c=conn.cursor()

def lookup_lemma_id(lemma_type):
    c.execute('select * from cwn_lemma where lemma_type="'+lemma_type+'"')
    cwn_lemma=c.fetchone()
    if cwn_lemma:
        lemma_id,cwn_pinyin,cwn_zhuyin,lemma_sno,lemma_type,meet_date,mod_time,supersense=cwn_lemma
        return lemma_type

def lookup_pos(sense_id):
    c.execute('select * from cwn_pos where cwn_id like "%'+sense_id+'%"')
    cwn_pos=c.fetchone()
    pos=cwn_pos[2]
    return pos

def lookup_lemma_type(lemma_id):
    c.execute('select * from cwn_lemma where lemma_id="'+lemma_id+'"')
    cwn_lemma=c.fetchone()
    if cwn_lemma:
        lemma_type=cwn_lemma[4]
        return lemma_type

def lookup_sense(lemma_id):
    c.execute('select * from cwn_sense where lemma_id="'+lemma_id+'"')
    cwn_sense=c.fetchone()
    sense_def=cwn_sense[2]
    return sense_def

def lookup_example(sense_id):
    c.execute('select * from cwn_example where cwn_id="'+sense_id+'"')
    cwn_example=c.fetchone()
    if cwn_example:
        cwn_id,example_sno,example_cont=cwn_example
        return ''.join(example_cont.split())

c.execute('select * from cwn_goodSynset')
for id,gloss,member,pwn_id,pwn_gloss,pwn_word,mod_time in c.fetchall():
    sense_id=member[:8]
    lemma_id=member[:6]
    pos=lookup_pos(sense_id)
    if pos:
        if pos in ['Na','Nb','Nc','Ncd','Nd','Ng','Nh','nom']: # N,V,A,D
            lemma=lookup_lemma_type(lemma_id)
            example=lookup_example(sense_id)
            if lemma and example:
                print pos,id,lemma.encode('utf8'),gloss.encode('utf8'),example.encode('utf8')
