import os
import sys

directory = 'C:\\Users\\yuki\\Documents\\案件\\タイ中古車システム\\souce code\\global-thai-nimbus-backend'

counter = 0
for folder, subs, files in os.walk(directory):
    for f in files:
        if f.endswith("java"):
            with open(folder + '\\' + f, 'r', encoding='utf-8') as content:
                for i, l in enumerate(content.readlines()):
                    if 'LOG.error(' in l:
                        counter += 1
                        print(f + ': at line' + str(i))
                        print('\t' + l.rstrip().replace(' ', ''))
print(str(counter) + ' error logs')
