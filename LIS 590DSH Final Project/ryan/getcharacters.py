# This script gets characters from books with IDs in the first column
# of the tab-separated file that Ryan Dubnicek provided.

# The characters could be contained in several different locations
# depending on when they were extracted.

import csv, os, shutil, json

allids = []
with open('/Users/tunder/Dropbox/courses/2017datasci/studentdata/DisabilityCorpusList_LIS590DSH_FinalProject.tsv', encoding = 'utf-8') as f:
    reader = csv.reader(f, delimiter = '\t')
    for row in reader:
        if len(row) < 1:
            print(len(row))
            continue
        anid = row[0]
        allids.append(anid)

post22dir = '/Volumes/TARDIS/work/characterdata/post1922hathi/fic/'
destination = '/Users/tunder/Dropbox/courses/2017datasci/studentdata/ryan/'
notfound = set()

# The post-1922 characters are aggregated in separate .book files.

for anid in allids:
    possiblepath = post22dir + anid + '.book'
    if os.path.isfile(possiblepath):
        destinationpath = destination + anid + '.book'
        shutil.copyfile(possiblepath, destinationpath)
    else:
        notfound.add(anid)

# But the pre-1922 characters are folded in massive multi-book files.

fourfold = ['/Volumes/TARDIS/work/characterdata/originaljsons/characterDataWithSpeech.txt', '/Volumes/TARDIS/work/characterdata/originaljsons/20thc_characters1.json', '/Volumes/TARDIS/work/characterdata/originaljsons/20thc_characters2.json', '/Volumes/TARDIS/work/characterdata/originaljsons/20thc_characters3.json']

errors = 0
gathered = []

for afile in fourfold:
    with open(afile, encoding = 'utf-8') as f:
        for line in f:
            jsonobject = json.loads(line)
            if 'id' in jsonobject:
                theid = jsonobject['id']
                if theid in notfound:
                    gathered.append(line)

            else:
                errors += 1


with open('/Users/tunder/Dropbox/courses/2017datasci/studentdata/ryan/earlychars.jsonl', mode = 'w', encoding = 'utf-8') as f:
    for g in gathered:
        f.write(g)



