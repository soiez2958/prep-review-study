import numpy as np

# 1. 다음 벡터를 생성하고 내적 계산
v1 = [1, 2, 3, 4]
v2 = [5, 6, 7, 8]


# 1-1. v1 과 v2를 만든다
v1 = np.array(v1) # array([1,2,3,4])
v2 = np.array(v2) # array([5,6,7,8])

# 1-2. np.dot() 또는 @ 연산자를 사용한다.
v3 = v1 @ v2

# 1-3. 결과 출력
print(v3)

# 1-4. 수동 검증
print("수동검증 = 1x5 + 2x6 + 3x7 + 4x8 ==> 5+12+21+32 => 17+53 = 70" )



# 2. 행렬 곱셈 수행

# 2-1. 2×3 행렬 A와 3×2 행렬 B 생성
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8], [9,10], [11,12]])

# 2-2. 행렬 곱셈 a @ b
c = a @ b

# 2-3. 결과 출력
print(c)

# 2-4. 수동 검증
print("수동 검증 : [ 1*7 + 2*9 + 3*11 ] => 7+18+33=58", "[ 1*8 + 2*10 + 3*12 ] => 8+20+36=64")
print("수동 검증 : [ 4*7 + 5*9 + 6*11 ] => 28+45+66=139", "[ 4*8 + 5*10 + 6*12 ] => 32+50+72=154")


# 3.벡터 노름 계산

# L1 노름 공식: |3| + |4| + |5|
# L2 노름 공식: √(3² + 4² + 5²)

# np.linalg.norm(벡터, np.inf)
# np.inf는 "무한대"를 의미한다.
# 이는 L∞ 노름을 계산하라는 뜻이다
# L∞ 공식: 값들 중 절댓값이 가장 큰 것

c = np.array([3, 4, 5])

L1 = np.linalg.norm(c, 1)
L2 = np.linalg.norm(c, 2)
L3 = np.linalg.norm(c, np.inf)  

print(int(L1), L2, int(L3))


# 4.조건부 인덱싱
# data = [1, 5, 3, 8, 2, 9, 4, 7, 6]

data = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])

# 4-1. 5보다 큰 값 추출
result1 = data[data > 5]
print(f"5보다 큰 수:{np.sort(result1)}")


# 4-2. 3 이상 7 이하 값 추출
result2 = data[(data >= 3) & (data <= 7)]
print(f"3 이상 7 이하의 수:{np.sort(result2)}")


# 4-3. 짝수 값 추출
result3 = data[data % 2 == 0]
print(f"짝수:{np.sort(result3)}")