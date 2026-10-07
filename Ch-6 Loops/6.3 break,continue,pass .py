#break completely stops the loop.

for i in range(1,100,2):
    if(i==67):
        break
    print(i)
    
    
# continue skips the current iteration and moves to the next one
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
#pass does nothing but contiue iteration without any disturbance
for i in range(0,45,5):
    if i==25:
        pass
    print(i)