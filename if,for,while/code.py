from random import *

person = 0
for i in range(1, 51):
    time=randrange(5,51)
    if 5<= time <=15:
        print("[o] %d번째 손님 (소요시간) : %d분" %(i,time))
        person+=1
    else:
        print("[ ] %d번째 손님 (소요시간) : %d분" %(i,time))

print("총 탑승 승객 : %d" %person)
    
