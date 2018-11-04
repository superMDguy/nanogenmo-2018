import re
import requests
from lxml import html
from time import sleep
from titlecase import titlecase
import json
from tqdm import tqdm

grimm_str = requests.get('http://www.gutenberg.org/files/2591/2591-0.txt'
                         ).content.decode('utf-8').replace('\r\n', '\n')
grimm_arr = grimm_str[2679:520288].replace(
    '\n\n\nIt also related', 'It also related').split('\n\n\n\n\n')

grimm = {}
for story in grimm_arr:
    title = titlecase(re.findall(r'[A-Z,\- ]{5,}', story)[0])
    grimm[title] = story[len(title):].strip()
    print(title)

code = requests.get('https://www.cs.cmu.edu/~spok/grimmtmp/').content.decode(
    'utf-8')
page = html.document_fromstring(code)

for link in tqdm(page.cssselect('ul a')):
    title = titlecase(link.text)

    if not title in grimm:
        grimm[title] = requests.get(
            f'https://www.cs.cmu.edu/~spok/grimmtmp/{link.get("href")}'
        ).content.decode('utf-8')
        tqdm.write(title)
        json.dump(grimm, open('grimm.json', 'w'))
        sleep(2)  # be nice ;)
