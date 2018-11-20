import cmudict
from tqdm import tqdm
import re

with open('cmu_pronouncing.txt', 'w') as f:
    only_stress = re.compile(r'[^012]')
    for word, phonemes in tqdm(cmudict.dict().items()):
        f.write(f"{word} {re.sub(only_stress, '', ''.join(phonemes[0]))}\n")
 
