# 문제 1번
def test1():
    import random
    Lst= [random.randint(1,100) for i in range(20)]
    Lst2=[random.randint(1,100) for i in range(20)]
    result=Lst+Lst2 #1.1
    print(result) 
    result=list(set(result)) #1.2
    print(result)
# 문제 2번    
def test2():
    import random
    
    student=[[chr(random.randint(65, 69)) for _ in range(10)] for _ in range(8)]
    print(student)
    answer=[chr(random.randint(65,69)) for _ in range(10)]
    print(answer)
    for i in range(8):
        count=0
        for j in range(10):
            if student[i][j]== answer[j]:
                count+=1
        print(f"{i} 번 학생의 정답 문항의 개수는 {count} 입니다.")
test1()
test2()

