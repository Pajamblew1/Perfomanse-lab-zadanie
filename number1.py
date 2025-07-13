import argparse
parse = argparse.ArgumentParser()
parse.add_argument("n")
parse.add_argument("m")
args = parse.parse_args()
a=[i+1 for i in range(int(args.n))]
i=0
j=0
print(a[0],end='')
while True:
    
    i+=1
    j=(j+1)%int(args.n)
    if i==int(args.m)-1:
        if a[j]==a[0]:
            break
        print(a[j], end='')
        i=0
print()

        
    
