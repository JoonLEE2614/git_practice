# -*- coding: utf-8 -*-

# class bankaccount:
#     def __init__(self, owner, balance): # balance = 0, balance 최소 값 설정
#         self.owner = owner
#         self.balance = balance
#
#     def deposit (self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f'입금이 완료되었습니다')  # (f'입금 완료. 현재 잔액: {self.balance}') 잔액 빠짐
#
#     def withdrawl (self, amount):
#         if 0 < amount <= balance:
#             self.balance -= amount
#             print(f'출금이 완료되었습니다.')  # 여기도 잔액 부분 빠짐
#
#             # else가 하나 들어가면 좋음 (else + print('출금 금액 부족')
#
#     def check_balance (self, balance): # 매개변수로 balance 받을 필요 없음 self쓰면 됨
#         print(f'잔액은 {balance} 입니다')  # self.balance 로 수정

class BankAccount:
    def __init__ (self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'입금 완료. 현재 잔액: {self.balance}')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'출금 완료. 현재 잔액: {self.balance}')
        else:
            print('출금 금액 부족')

    def check_balance(self):
        print(f'잔액은 {self.balance}입니다.')

# Test
account = BankAccount('Tim', 3000)
account.deposit(300)
account.withdraw(1000)
account.check_balance()

