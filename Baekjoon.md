## 백준 문제/풀이 정리   

### 2675번   

(예제입력)   
2     
3 ABC    
5 /HTP    
    
(예제출력)    
AAABBBCCC    
/////HHHHHTTTTTPPPPP    
    
(코드)    
```
su=int(input())      
for i in range(su):    
    a, b=  input().split()
    for j in b:                           
        print(j*int(a) , end="")    
    print()
```

 
