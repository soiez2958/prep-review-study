import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def problem_1_4():

    # 타이타닉 데이터 로드
    titanic = sns.load_dataset('titanic')
    print("타이타닉 데이터 정보:")
    print(f"데이터 형태:{titanic.shape}")
    print(f"주요 열:{titanic.info()}")
    print(f"결측값 확인:{titanic.head()}")

    # 좌석 등급별 생존율 분석
    print("좌석 등급별 생존율:")
    df1 = titanic.groupby('pclass')['survived'].mean()
    for pclass, rate in df1.items():
        print(f"{pclass}등석: {rate:.3f} ({rate*100:.1f}%)")


    # 성별 좌석 등급별 다중 집계
    print("성별 좌석 등급별 생존율")
    df2 = titanic.groupby(['sex', 'pclass']).agg(
        {
            'age': ['mean', 'std', 'count'],
            'fare': ['max', 'min', 'mean'],
            'survived': 'mean'        
        }
    ).round(2)
    print(df2)

    # 피벗 테이블 생성
    print("피벗 테이블")
    
    # 성별과 좌석등급별 생존율 피벗 테이블
    sex_survival_pivot = titanic.pivot_table(
        values='survived', 
        index='sex', 
        columns='pclass', 
        aggfunc='mean'
    ).round(3)
    
    print("성별-좌석등급별 생존율 피벗 테이블:")
    print(sex_survival_pivot)
    print()
    

    # 시각화
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    # 좌석등급별 생존율 막대 그래프
    df1.plot(kind='bar', ax=axes[0, 0], color='skyblue')
    axes[0, 0].set_title('좌석등급별 생존율')
    axes[0, 0].set_xlabel('좌석등급')
    axes[0, 0].set_ylabel('생존율')
    axes[0, 0].set_xticklabels(['1등석', '2등석', '3등석'], rotation=0)

    # 성별-좌석등급별 생존율 히트맵
    sns.heatmap(sex_survival_pivot, annot=True, cmap='RdYlBu_r', ax=axes[0, 1])
    axes[0, 1].set_title('성별-좌석등급별 생존율')

if __name__ == "__main__":
    results = problem_1_4()