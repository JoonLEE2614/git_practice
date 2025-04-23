class Fibonacci:
    def __init__(self, n):
        self.n = n # 객체 생성 시 피보나치 수의 위치를 설정

    def calculate(self):
        if self.n <=1: # n이 0 또는 1일 경우
            return self.n 

        a,b = 0,1
        
# n번째 피보나치 수를 구하기 위한 반복문 
        for i in range(self.n-1): # 2번째 항부터 n번째 항까지 계산
            a, b = b, a+b
        return b   # n번째 피보나치 수 반환


fibonacci = Fibonacci(10)
print(f'The 10th Fibonacci number is: {fibonacci.calculate()}')
