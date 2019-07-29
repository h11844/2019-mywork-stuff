# coding: utf-8
#3筆資料
#1011 11101
#100111 111010
#1101 110001

n =int(input())

for i in range(n):
    line =input()
    a,b = line.split()
    s= int(a,2)+int(b,2)
    print(a,b, bin(s)[2:])
