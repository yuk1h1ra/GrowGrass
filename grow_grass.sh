#! /bin/bash

cd ~/GrowGrass/
echo "w" >> grasses.txt
git add grasses.txt
git commit -m "w"
git push origin master
