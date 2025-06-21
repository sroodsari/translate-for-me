#!/Users/susanroodsari/Documents/Code/translator-react-app/backend/env/bin/python3.10
from __future__ import print_function

import fileinput
import epitran

epi = epitran.Epitran('uig-Arab')
for line in fileinput.input():
    s = epi.transliterate(line.strip().decode('utf-8'))
    print(s.encode('utf-8'))
