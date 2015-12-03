
d=dict()

for line in open('cwn_dirty.uniq'):
    lemma_name,definition=line.split()
    if lemma_name not in d:d[lemma_name]=set([definition])
    else:d[lemma_name].add(definition)

all_lemma_names=set()
for lemma_name,definitions in d.items():
    all_lemma_names.add(lemma_name)

def definitions(lemma_name):
    return d[lemma_name]

class Synset:
    def __init__(self,lemma_name_index):
        lemma_name,index=lemma_names_index.split('.')
        self.definitions=['animal','canine']

def synsets(lemma_name):
    synset_list=[]
    for definition in d[lemma_name]
