
students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}
]

## 문제 3.가장 높은 평균 점수를 가진 학생을 찾는 함수

# 가장 높은 평균 점수를 가진 학생을 찾는 함수

def find_top_student(students):

    for student in students:
        scores = list(student["subjects"].values())
        average = sum(scores) / len (scores)
        student["average"] = average
        print(f"{student['name']}의 평균 점수:{average:.2f}") 


    top_student = max(students, key=lambda s:['average'])
    print(f"가장 높은 평균 점수를 받은 학생 {top_student['name']}이며, "
    f"점수는 {top_student['average']:.2f}점입니다.")

find_top_student(students) 