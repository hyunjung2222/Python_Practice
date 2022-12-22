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
    **for j in b:   숫자 반복이 아니라 문자열에서 요소를 꺼낼수도 있음!!**                          
        print(j*int(a) , end="")    
    print()
```

 
