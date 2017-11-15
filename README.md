# GrowGrass
毎日１回pushをして、芝生生やす

## crontab
crontabの定時実行を用いて、実行する
```
$ crontab -e  
```
```
0 12 * * * ~/GrowGrass/grow_grass.sh > /dev/null
```
