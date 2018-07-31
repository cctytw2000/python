
  
import random   #匯入模組
# random.randint(a,b)
# 回傳一個整數i a<=i<=b

math1= random.randint(1,100)
while True:
    math0=int(input('請輸入數字:'))
    if math0 > math1:
           print("太高")
    elif math0 < math1:
           print("太低")
    else :
        print("賓果")
        break
        
           
 


        
    



    
   





