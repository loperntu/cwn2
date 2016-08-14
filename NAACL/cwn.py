#moe.py
d=dict()
name='cwn_dirty_examples_20151007.tsv'
name='cwn_dirty_threshold0.tsv'
name='cwn_dirty.csv'
for line in open(name):
    lemma_name,definition=line.split(',')#,example=line.split()
    lemma_name=lemma_name.strip().replace('.','')
    definition=definition.strip()
#    example=example.strip()
    if lemma_name not in d:d[lemma_name]=[definition]#,example)]
    else:d[lemma_name].append(definition)#,example))

all_lemma_names=[lemma_name for lemma_name in d]

class Synset:
    def __init__(self,lemma_name_index):
        lemma_name,index=lemma_name_index.split('.')
        self.lemma_name=lemma_name
        self.definition=d[lemma_name][int(index)]#[0]
#        self.example=d[lemma_name][int(index)][1]
        self._name=lemma_name_index
    def __repr__(self):
        return "%s('%s')" % ('cwn.Synset',self._name)

def synset(lemma_name_index):
    return Synset(lemma_name_index)

def synsets(lemma_name):
    synset_list=[]
    for i in range(len(d[lemma_name])):
        lemma_name_index='%s.%d' % (lemma_name,i)
        synset_list+=[synset(lemma_name_index)]
    return synset_list

if __name__=='__main__':
    for lemma_name in all_lemma_names:
        for s in synsets(lemma_name):
            print s,s.definition#,s.example
