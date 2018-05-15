items = {"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
s = 0
while True:
          name = input("제품명: ")
          if name in items:
               s = s + items[name]
               print("[%s:%d]>%d"%(name,items[name],s))
          elif s =="":
               print("총금액: ",s)
               break
          else:
               print(name,"은 미등록 제품입니다.")
