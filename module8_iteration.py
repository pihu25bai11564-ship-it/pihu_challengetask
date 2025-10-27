for i in range (1,6):
     print(i,end="")
print() 
#while loop
n = 1
while n <= 5:
     print(n*2,end="")
     n += 1
print()   
#break and continue 
for i in range(1,8):
     if i == 5:
          continue
     if i == 7:
          break
     print(i,end="")       