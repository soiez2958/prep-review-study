## 주제 2: 리스트와 딕셔너리를 활용한 학생 성적 관리 시스템
# 학생들의 성적 데이터를 관리하는 시스템을 만드세요:

# 주어진 데이터 구조
students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}
]

## 문제 1.각 학생의 평균 점수를 계산하여 딕셔너리로 반환하는 함수

# 각 학생의 평균 점수를 계산하여 딕셔너리로 반환하는 함수
for student in students:
    scores = list(student["subjects"].values())
    average = sum(scores) / len (scores)
    print(f"{student['name']}의 평균 점수:{average:.2f}") 
    # dict: {학생이름: 평균점수} 형태의 딕셔너리

#   평균 점수의 데이터의 값을 리스트에서 딕셔너리로 변환
dict(student)


