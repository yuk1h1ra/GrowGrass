# -*- coding: utf-8 -*-
import os

os.system('cd ~/GrowGrass')

f = open('grasses.txt', 'a')
f.write('w')
f.close

os.system('git add grasses.txt')
os.system('git commit -m "w"')
os.system('git push origin master')
