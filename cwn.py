class Lemma:
    def __init__(self,lemma_name):
        self.lemma=lemma_name
        self.definitions=['animal','canine']

d=dict()

for line in open('cwn_dirty.uniq'):
    lemma_name,definition=line.split()
    if lemma_name not in d:d[lemma_name]=set([definition])
    else:d[lemma_name].add(definition)

all_lemma_names=set()
for lemma_name,definitions in d.items():
    all_lemma_names.add(lemma_name)
#    for definition in definitions:
 #       print lemma_name,definition

#for lemma_name in all_lemma_names:
 #   print lemma_name

def definitions(lemma_name):
    return d[lemma_name]
