## 차량 함수 
# 문제:
# Car라는 클래스를 정의하고, 이 클래스는 자동차의 make(제조사), model(모델), year(제조 연도)를 속성으로 가져야 한다. 또한 이 클래스는 다음과 같은 메서드를 가져야 한다:
# display_info: 자동차의 정보(제조사, 모델, 연도)를 출력하는 함수.
# update_year: 자동차의 연도를 1년 증가시키는 함수.


## 내 풀이

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'이 차는{self.make}회사의 {self.model} 이고 {self.year}년에 제조 되었습니다.')

    def update_year(self):
        self.year += 1
        print(f'이 차는 {self.year}년에 제조 되었습니다.')


## 예시

car1 = Car('HyunDai', 'Sonata', 1998) ## 이부분 오류(기존 '1998'에서 1998로 수정함) 
car1.display_info()
car1.update_year()


## Gpt 답 (틀린 부분만)

# 1. car1 = Car('HyunDai', 'Sonata', '1998')에서 year 값이 문자열 '1998'로 입력되고 있어. 이 값은 정수형으로 수정해야 해.



