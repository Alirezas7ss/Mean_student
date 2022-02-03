
import csv
from ctypes import LibraryLoader
import statistics
#for need to mean so import mean in statistics Library
from statistics import mean
d={}
with open("s1.csv") as f:
  reader=csv.reader(f)
  for row in reader:
    h=[]
    name=row[0]
    grade=[]
    sum=0
    h.append(name)
    for ro in row[1:]:
      grade.append(int(ro))
    h.append(mean(grade))
    d[h[0]]=h[1]
  #c=dict(sorted(d.items(), key=lambda item: item[1]  ))
  #new_list = list(map(list, c.items()))
  #print(new_list)
  #all_mean=[]
  #for i in c:
  #  all_mean.append(c.values)
all_mean=mean(d.values())
t = open("s2.csv", 'a')
t.write("{}\n".format(all_mean))
