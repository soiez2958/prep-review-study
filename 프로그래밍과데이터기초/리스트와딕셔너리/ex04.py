students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}
]

## 문제 2.모든 과목에서 80점 이상인 학생들의 이름을 리스트로 반환하는 함수

def find_excellent_students(students, threshold=80):
    excellent_students = []  

    for student in students:
            scores = list(student["subjects"].values())
            
            if min(scores) >= threshold:
                # 3. 모든 과목이 80점 이상이라면 이름을 리스트에 추가합니다.
                excellent_students.append(student["name"])
                
    return excellent_students

result = find_excellent_students(students, 80)
print(f"우수 학생 명단: {result}")