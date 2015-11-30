for line in open('group-evaluation.csv'):
    if line.split(',')[0] in ['1','2','3','4','5']:
        print ' '.join(line.split(',')[:3])
