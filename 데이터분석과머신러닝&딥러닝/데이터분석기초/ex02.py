import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def problem_1_3():
    print("=== 문제 1.3: Pandas DataFrame 생성 및 조건부 인덱싱 ===")
    
    # 1. 딕셔너리를 이용한 DataFrame 생성
    np.random.seed(42)    
    
    
    data = {
            'name': ['김철수', '이영희', '박민수', '최지영', '정태현', '한소희', '윤상호', '배수진'],
            'age': [25, 30, 35, 28, 42, 31, 29, 27],
            'city': ['서울', '부산', '대구', '서울', '광주', '서울', '부산', '대구'],
            'salary': [3500, 4200, 3800, 4500, 5200, 3900, 3600, 4100],
            'department': ['개발', '마케팅', '개발', '기획', '개발', '마케팅', '기획', '개발'],
            'experience': [2, 5, 8, 3, 12, 6, 4, 3]
        }

    df = pd.DataFrame(data)
    
    # 2. 단일 조건 필터링
    print("단일 조건 필터링")
    # 나이가 30이상인 직원
    age_list = df['age']  >= 30
    print(f"나이가 30 이상인 직원:\n{df.loc[age_list, 'name']}")
    print(f"{age_list.sum()}명")

    # 특정 도시(예: 서울) 거주 직원 찾기
    city_list = df['city'] == "서울"
    print(f"서울에 거주하는 직원:\n{df.loc[city_list, 'name']}")

    # 급여가 4000 이상인 직원 필터링
    salary_list = df['salary'] >= 4000
    print(f"급여가 4000 이상인 직원:\n{df.loc[salary_list, 'name']}")
    print(f"{salary_list.sum()}명")


    # 3. 복합 조건 필터링
    print("복합 조건 필터링")

    # AND 연산: 서울 거주 **AND** 급여 4000 이상
    target_people1 = df[(df['city'] == "서울") & (df['salary'] >= 4000)]
    print(f"서울에 거주하고 급여가 4000 이상인 직원:{target_people1}")
        
    # OR 연산: 개발팀 **OR** 급여 4500 이상
    target_people2 = df[(df['department'] == "개발") | (df['salary'] >= 4500)]
    print(f"개발팀이거나 급여가 4500이상인 직원:{target_people2}")

    # NOT 연산: 개발팀이 아닌 직원
    target_people3 = df[df['department'] != "개발"]
    print(f"개발팀이 아닌 직원:{target_people3}")


    # 4. 기본 통계 및 집계
    print("기본 통계 및 집계")
    #  부서별 평균 급여 계산
    print(df.groupby(['department'])['salary'].mean())

    # 도시별 직원 수
    print("\n도시별 직원 수 : ")
    print(df['city'].value_counts())

    # 경력 통계 분석
    print("\n경력 통계 분석 : ")
    print(df['experience'].describe())

if __name__ == "__main__":
    results = problem_1_3()