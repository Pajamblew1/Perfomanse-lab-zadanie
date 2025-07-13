import argparse
array=[]
parse = argparse.ArgumentParser()
parse.add_argument("FileName")
args = parse.parse_args()
file = open(args.FileName)
count =0
summ=0
for line in file:
    array.append(int(line))
array.sort()
if len(array)%2==0:
    median = (array[int(len(array)/2)-1]+array[int(len(array)/2)])/2
else:
    median = (array[int(len(array)/2)])
for num in array:
    summ+=abs(num-median)
print(summ)

