s = 0
while s!="":
     eng = input("영어 단어: ")
     kor = input("한글 단어: ")
     if eng in kor:
          engkor_dict = dict()
          engkor_dict[eng] = kor
          break          
     
print(engkor_dict)
