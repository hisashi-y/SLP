dict = {}
tag = '<s>'
i = 10
dict[f'{i} {tag}'] = 100

s = 10
tag2 = '<s>'

dict[f'{i} {tag}'] == dict[f'{s} {tag2}']
