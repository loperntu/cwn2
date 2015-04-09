janice_supersense={
'3':'noun.Tops',
'4':'noun.act',
'5':'noun.animal',
'6':'noun.artifact',
'7':'noun.attribute',
'8':'noun.body',
'9':'noun.cognition',
'10':'noun.communication',
'11':'noun.event',
'12':'noun.feeling',
'13':'noun.food',
'14':'noun.group',
'15':'noun.location',
'16':'noun.motive',
'17':'noun.object',
'18':'noun.person',
'19':'noun.phenomenon',
'20':'noun.plant',
'21':'noun.possession',
'22':'noun.process',
'23':'noun.quantity',
'24':'noun.relation',
'25':'noun.shape',
'26':'noun.state',
'27':'noun.substance',
'28':'noun.time'
}

for line in open('goodSynset_Nabcd_ID_Lemma_Gloss_Example_800.tsv'):
    janice,iju,pos,id,lemma,gloss,example=line.split()
    janice=janice_supersense[janice]
    if janice!=iju:print janice,iju,pos,id,lemma,gloss,example
    else:print
