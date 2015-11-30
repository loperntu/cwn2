from Levenshtein import distance

cwn_dict={}
for line in open('cwn_dirty.csv').readlines():
    lemma_type,sense_def=line.split(',')
    lemma_type,sense_def=lemma_type.strip(),sense_def.strip()
    if lemma_type not in cwn_dict:cwn_dict[lemma_type]=[sense_def]
    else:cwn_dict[lemma_type].append(sense_def)

moe_dict={}
for line in open('dict-revised.csv').readlines():
    title,definition=line.split(',')
    title,definition=title.strip(),definition.strip()
    if title not in moe_dict:moe_dict[title]=[definition]
    else:moe_dict[title].append(definition)

for word in moe_dict:
    if word in cwn_dict:
        sense_rank={}
        for moe_sense in moe_dict[word]:
            max=0
            for cwn_sense in cwn_dict[word]:
                d=distance(moe_sense,cwn_sense)
                if d>max:max=d
            sense_rank[moe_sense]=max
        for sense,rank in sorted(sense_rank.items(),key=lambda x:x[1],reverse=True):
            print word,sense
