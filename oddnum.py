low=int(input("Low: "))
high=int(input("High: "))
odd=0
for i in range(low,high+1):
    if i%2!=0:
        odd+=1

print("number of odd numbers bw low and high are :",odd)