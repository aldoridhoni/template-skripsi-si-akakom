#!/usr/bin/python
# Taken from http://tex.stackexchange.com/questions/24397/extract-document-statistics-how-many-pages-has-chapter-xy-count-fixmes/24480#24480
import re, os

chap_list = []
end = 40
front_matter = 13

with open('main.toc') as file:
    for l in file:
        #if (not '{part}' in l) and (not '{section}' in l): continue
        m = re.match(r'^\\contentsline\W*{(section|part|chapter)}{(.*)}{([0-9]+)}({[^}]*})?$',l)
        if not m: continue
        print('Match:',m.group(1, 2, 3))
        type, raw, page = m.group(1, 2, 3)
        if type == 'chapter':
            m = re.match(r'^\\numberline\W*{([0-9]+)}(.*)$',raw)
            if not m: continue
            num, raw = m.group(1,2)
            raw = re.sub(r'\\FN@sf@gobble@opt .*$','',raw) # strip footnote
            raw = re.sub(r'\\IeC\W*{.*?([a-zA-Z]) ?}',r'\1',raw) # remove accents
            raw = re.sub(r'\\emph\W*{(.*?)}',r'\1',raw) # remove \\emph
            raw = re.sub(r'(:|\W*\\&|\W*\().*$','',raw) # take just the "first part" as name
            raw = re.sub(r' a ',r' ',raw) # remove 'a' as conjunction
            raw = re.sub(r'[^a-zA-Z]+','_',raw) # remove commans
            raw = raw.lower()
    
            chapter = {'page': int(page), 'name': raw, 'number': int(num)}
            chap_list.append(chapter)

for index, chapter in enumerate(chap_list):
    print(chapter)
    start = chapter['page'] + front_matter
    if index + 1 < len(chap_list):
        next_chapter = chap_list[index + 1]['page']
        end = next_chapter - 1 + front_matter
    else:
        end = 'end'
    
    try:
        spec = "{}-{}".format(start, end)
        print(spec)
        out = "split/{}.pdf".format(chapter['name'])
        os.system('pdf-stapler cat pdf/skripsi.pdf %s "%s"' % (spec, out))
    except Exception as e:
        print(e)
