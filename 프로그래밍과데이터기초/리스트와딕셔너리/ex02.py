# 주어진 데이터 구조

students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}
]
# 2. 특정 과목의 전체 학생 평균을 계산하는 함수
def calculate_subject_average(students, subject_name):

    total = 0
    count = len(students)

    for student in students:
        score = student["subjects"][subject_name]
        total += score
    return total / count

result = calculate_subject_average(students , "수학")
print(f"수학 과목 전체 평균: {result}")




# 특정 과목의 전체 학생 평균을 계산하는 함수
