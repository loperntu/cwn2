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

for word in cwn_dict:
    if word in moe_dict:
        sense_list=cwn_dict[word]

        print 'cwn:'
        for i in range(len(sense_list)):
            print sense_list[i]
            pass

        print 'moe:'
        for moe_sense in moe_dict[word]:
            print moe_sense

            i=flag=0
            while i<len(sense_list):
       #     for i in range(len(sense_list)):
                if distance(sense_list[i],moe_sense)<30:
                    if flag:sense_list.pop(flag)
                    else:flag=i
                i+=1

        print 'merged:'
        for sense in sense_list:
            print word,',',sense

        print
