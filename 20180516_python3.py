s = int(input("점수: "))
if 90 <= s <=100:
     print(s, ":A")
elif 80 <= s <= 89:
     print(s ,":B")
elif 70 <= s <= 79:
     print(s, ": C")
elif 60 <= s <= 69:
     print(s, ": D")
elif 0 <= s <= 59:
     print(s,": F")
else:
     print("입력 가능한 점수 범위는 0 ~ 100 입니다.")
