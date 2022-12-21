백준 문제/풀이 정리   
====

**2675번**   

(예제입력)   
2     
3 ABC    
5 /HTP    
    
(예제출력)    
AAABBBCCC    
/////HHHHHTTTTTPPPPP    
    
(코드)    
su=int(input())        
for i in range(su):        
    a, b=  input().split()        
    for j in b:         **굳이 숫자가 아니더라도 문자열의 요소로도 반복으로 쓸수 있음!!**    
        print(j*int(a) , end="")        
    print()    
    
 
