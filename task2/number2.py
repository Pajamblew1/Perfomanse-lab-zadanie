import argparse
parse = argparse.ArgumentParser()
parse.add_argument("tochki")
parse.add_argument("okr")
args = parse.parse_args()
f=open(args.tochki)
g=open(args.okr)
data=[]
data1=[]
for line in f:
        data.append([float(x) for x in line.split()])
for line in g:
    data1.append([float(x) for x in line.split()])
for i,point in enumerate(data,1):
    if ((point[0]-data1[0][0])**2+(point[1]-data1[0][1])**2)==(data1[1][0])**2:
        print("0")
    elif ((point[0]-data1[0][0])**2+(point[1]-data1[0][1])**2)>(data1[1][0])**2:
        print("2")
    else:
        print("1")
