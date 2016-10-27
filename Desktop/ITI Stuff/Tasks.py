s = '''It was the best of times, it was the worst of times;
it was the age of wisdom, it was the age of foolishness;
it was the epoch of belief, it was the epoch of incredulity;
it was ...'''

n= s.replace('.',' ')
k = n.replace(',',' ')
z = k.replace(';',' ')
news = z.replace('\n',' ')

