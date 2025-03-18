'''
    학생 관리 프로그램

    학생의 인적 사항을 등록 후 검색하는 프로그램을 만드시오
    (학번, 이름, 생년월일, 학년 등을 변수로 갖는 class 생성)

    아래의 메뉴 중 종료를 제외한 메뉴가 각각의 함수 및 메서드로 동작되도록 코드 작성
    1. 인적사항 등록    2. 학생 검색    3. 학생 정보 수정
    4. 학생 정보 삭제   5. 전체 학생 목록   6. 종료

    * 참고사항
     1. 데이터베이스가 없는 관계로 학생 정보는 딕셔너리에 저장
        (ex. 딕셔너리명 = {학번 : 학생정보 객체, 학번 : 학생정보 객체 ...})

    2. 변수나 객체의 이름을 지정할 때 globals() 함수를 사용하여
       변수나 객체 이름에 다른 변수의 데이터를 사용할 수 있다
        ex.
            for i in range(1,4) :
                globals()[f"var{i}] = 0
            print(var1, var2, var3)
'''
class student :
    def __init__(self, num, name, birth, grade) :
        self.num = num
        self.name = name
        self.birth = birth
        self.grade = grade

    def birthSplit(self) :
       return self.birth.split("/")

def choiceJob() :   # 동작 선택
    while True :
        print("학생 관리 프로그램\n메뉴를 선택하세요.\n1. 인적사항 등록\n2. 학생 검색\n3. 학생 정보 수정\n4. 학생 정보 삭제\n5. 전체 학생 목록\n6. 프로그램 종료\n>>>")
        try :
            a=int(input("메뉴 선택 : "))
        except :
            pass
        print()
        if a in range(1,7) :
            return a
        else :
            print("올바른 메뉴를 선택하세요(1 ~6)\n")

def add() :     # 학생 정보 등록
    num=input("학번입력 : ")
    name=input("학생 이름 : ")
    birth=input("생년월일(yyyy/mm/dd) : ")
    grade=0
    while True :
        try :
            grade= int(input("학년(1~3) : "))
        except :
            pass
        if grade in (1,2,3):
            break
        else :
            print("1~3 범위의 숫자를 입력하세요")
    print()
    if dic.get(num)==None :
        globals()[f"{num}"] = student(num,name,birth,grade)
        dic[num] = globals()[f"{num}"]
        print("새로운 학생 정보가 등록되었습니다.")
    else :
        print(f"학번이 {num}인 학생 정보는 이미 존재합니다.")

def search() :       # 학생 검색
    while True :
        try :
            num = input("검색할 학생의 학번 : ")
        except :
            pass
        else :
            if num in dic.keys() :
                birthLs = dic[num].birthSplit()
                print("============ 학생 정보 ============")
                print(f"학번\t : {num}\n이름\t : {dic[num].name}")
                print(f"학년\t : {dic[num].grade}")
                print(f"생년월일 : {birthLs[0]}년 {birthLs[1]}월 {birthLs[2]}일")
                
            else :
                print(f"존재하지 않는 학번 : {num}")
        
        break

def revise() :      # 학생 정보 수정
    while True :
        num = input("수정할 학생의 학번 : ")
        if num in dic.keys() :
            while True :
                try :
                    cho = int(input("1. 학번\n2. 이름\n3. 생년월일\n4. 학년\n>>> "))
                except :
                    pass
                else :
                    if cho not in (1,2,3,4) :
                        continue
                    else :
                        break
            if cho == 1 :       # 학번 수정
                name = dic[num].name
                birth = dic[num].birth
                grade = dic[num].grade
                while True :
                    newnum = input("새로운 학번 입력 : ")
                    if newnum in dic.keys() :
                        print("이미 존재하는 학번입니다")
                    else :
                        break
                dic.pop(num)
                globals()[f"{newnum}"]=student(newnum,name,birth,grade)
                dic[newnum] = globals()[f"{newnum}"]
            elif cho == 2 :     # 이름 수정
                name = input("새 이름 입력 : ")
                dic[num].name = name
            elif cho == 3 :    # 생년월일 수정
                birth = input("생년월일(yyyy/mm/dd) : ")
                dic[num].birth = birth
            elif cho == 4 :     # 학년 수정
                birth = input("생년월일(yyyy/mm/dd) : ")
                dic[num].grade = grade
            print("수정 완료")
            break
        else :
            print("그런 학번은 없습니다.\n")

def delete() :      # 학생 정보 삭제
    while True :
        try :
            sel = int(input("1. 선택 삭제\n2. 전체 삭제\n>>> "))
        except :
            pass
        else : 
            if sel==1 or sel==2 :
                break
            else :
                continue
    if sel==1 :
        while True :
            num = input("삭제할 학생의 학번 : ")
            if num in dic.keys() :
                dic.pop(num)
                print("삭제가 완료되었습니다.")
                break
            else :
                print("그런 학번은 없습니다\n")

    elif sel==2 :
        dic.clear()
        print("전체 학생 목록이 삭제되었습니다.")

def info() :        # 전체 학생 출력
    for num in dic.keys() :
        birthLs = dic[num].birthSplit()
        print("==================================")
        print(f"학번\t : {num}\n이름\t : {dic[num].name}")
        print(f"학년\t : {dic[num].grade}")
        print(f"생년월일 : {birthLs[0]}년 {birthLs[1]}월 {birthLs[2]}일")
    print("==================================")

dic = {}
while True :
    cho = choiceJob()
    if cho==1 :
        add()

    elif cho==2 :
        search()

    elif cho==3 :
        revise()

    elif cho==4 :
        delete()

    elif cho==5 :
        info()

    elif cho==6 :
        print("프로그램을 종료합니다")
        break
    
    print()