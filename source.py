import csv
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
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
    for key,value in d.items():
      t = open("s2.csv", 'a')
      t.write("{},{}\n".format(key,value))


def calculate_sorted_averages(input_file_name, output_file_name):
  d={}
  with open(input_file_name) as f:
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
    c=dict(sorted(d.items(), key=lambda item: item[1] ))
    for key,value in c.items():
      t = open(output_file_name, 'a')
      t.write("{},{}\n".format(key,value))



def calculate_three_best(input_file_name, output_file_name):
  d={}
  with open(input_file_name) as f:
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
    c=dict(sorted(d.items(), key=lambda item: item[1] , reverse=True ))
    for key,value in c.items():
      t = open(output_file_name, 'a')
      t.write("{},{}\n".format(key,value))
      sum+=1
      if sum==3:
        break

def calculate_three_worst(input_file_name, output_file_name):
  d={}
  with open(input_file_name) as f:
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
    c=dict(sorted(d.items(), key=lambda item: item[1]))
    for key,value in c.items():
      t = open(output_file_name, 'a')
      t.write("{}\n".format(value))
      sum+=1
      if sum==3:
        break


def calculate_average_of_averages(input_file_name, output_file_name):
  d={}
  with open(input_file_name) as f:
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
    all_mean=mean(d.values())
    t = open(output_file_name, 'a')
    t.write("{}\n".format(all_mean))