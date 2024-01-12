import math

t = int(input())
for counter in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    growth = list(map(int, input().split()))
    order = list(map(int, input().split()))
    L = zip (height,growth,order)
    order, growth, height = zip(*sorted(zip(order,growth,height)))

    order = list(order)
    growth = list(growth)
    height = list(height)

    days = [0] * int(n)

    ok = True
    for i in range(n-1):
        if height[i] < height[i+1]:
            grodiff = growth[i]-growth[i+1]
            heightdiff = height[i+1]-height[i]
            if grodiff < 1:
                ok = False
                break
            else:
                addthis = 0
                if heightdiff%grodiff == 0:
                    addthis = math.ceil(heightdiff/grodiff)+1
                else:
                    addthis = math.ceil(heightdiff/grodiff)
                
                days[i] = addthis
        elif height[i] == height[i+1] and growth[i]-growth[i+1] == 0:
            ok = False
            break
    
    if ok == False:
        print(-1)
    else:
        temp = max(days)
        for i in range(n):
            height[i] += growth[i]*temp
        
        sortedl = []
        
        for i in range(n):
            sortedl.append(height[i])
        
        sortedl.sort(reverse = True)
        
        for i in range(n):
            if sortedl.index(height[i]) != order[i]:
                ok = False
                break
        
        if ok == False:
            print(-1)
        else:
            print(temp)
        
        
