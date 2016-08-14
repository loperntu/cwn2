from sys import argv
import cwn,moe,Levenshtein

threshold=int(argv[1])
for lemma in cwn.all_lemma_names:
    sense_list=cwn.synsets(lemma)
    if lemma in moe.all_lemma_names:
        for moe_sense in moe.synsets(lemma):
            i=flag=0
            while i<len(sense_list):
                if Levenshtein.distance(moe_sense.definition,sense_list[i].definition)<threshold:
                    if flag:
#                        print moe_sense.definition,
 #                       print Levenshtein.distance(moe_sense.definition,sense_list[i].definition),sense_list[i].definition,
  #                      print Levenshtein.distance(moe_sense.definition,sense_list[flag].definition),sense_list.pop(flag).definition
                        sense_list.pop(flag)
                    else:flag=i
                i+=1
    for sense in sense_list:print sense.lemma_name,sense.definition#,sense.example
