from sys import argv
import cwn,moe,Levenshtein

threshold=int(argv[1])
for lemma in cwn.all_lemma_names:
    sense_list=cwn.synsets(lemma)
    if lemma in moe.all_lemma_names:
        for moe_sense in moe.synsets(lemma):
            i=flag=0
            while i<len(sense_list):
                if Levenshtein.distance(sense_list[i].definition,moe_sense.definition)<threshold:
                    if flag:sense_list.pop(flag)
                    else:flag=i
                i+=1
    for sense in sense_list:print sense.lemma_name,sense.definition
