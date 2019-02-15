import heapq
from heapq import heappop
import pygame
from  time import sleep

def findAverageWT(sum_k,sum_h,finish,n):
    s1=sum(finish)
    s2=sum_h
    s3=sum_k
    avg=(s1-s2-s3)/n
    return avg

def findClosestAT(current_time,h):
    for at in h:
        z=at-current_time
        if(z>0):
            return int(at)

q=[]
h=[]
k=[]
allowed_bt=[]
allowed_at=[]
index=0
at_list=[]
bt_list=[]

n=int(input('How many processes are required?'))

for i in range(0,n):
    a = int(input('Enter Arrival time: '))
    b = int(input('Enter Burst time : '))
    heapq.heappush(q, (a, b))
for i in range(0, n):
    k.append(q[i][1])
for i in range(0,n):
    h.append(heappop(q)[0])

sum_k=sum(k)
sum_h=sum(h)
k.reverse()
hh=heapq.heappop(h)
allowed_at=[0,hh]
allowed_bt=[]
finish=[]

commence=[0,hh]
current_time=[0,hh]
allowed_at.append(heapq.heappop(h))
kp=k.pop()
allowed_bt.append(kp)

while(k):
    allowed_bt.sort()
    at = allowed_at[-1]
    bt = allowed_bt[0]
    if(allowed_at[-1]-allowed_at[-2]<bt):
        current_time.append(at)
        heapq.heappop(allowed_bt)
        allowed_bt.append(bt-at+current_time[-2])
        ap=k.pop()
        allowed_bt.append(ap)
        allowed_bt.sort()
        if(len(h)!=0):
           allowed_at.append(heapq.heappop(h))
    else:
        current_time.append(current_time[-1]+bt)
        finish.append(current_time[-1])
        heapq.heappop(allowed_bt)

    if (len(allowed_bt) == 0 and len(h) == 0):
        break

    if(len(allowed_bt)==0 and len(h)!=0):
        allowed_at.append(heapq.heappop(h))
        allowed_bt.append(k.pop())
        current_time.append(at)

allowed_bt.reverse()
for i in range(len(allowed_bt)):
    finish.append(current_time[-1]+allowed_bt.pop())
    current_time.append(finish[-1])
if(len(h)==0 and len(k)!=0 ):
    finish.append(allowed_at[-1]+k[-1])
    current_time.append(finish[-1])

print(finish)
print(current_time)
avg=findAverageWT(sum_k,sum_h,finish,n)
print(avg)


pygame.init()
screen = pygame.display.set_mode((1800, 900))
done = False
is_blue = True
x = 0
y = 400

for j in range (len(current_time)-1):
    color = (255,255,255)
    for i in range((current_time[j])*10,(current_time[j+1])*10):
        x += 1
        pygame.draw.rect(screen, color, pygame.Rect(x, y,1,75))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, 1, 75))



pygame.display.flip()
sleep(60)
pygame.quit()
