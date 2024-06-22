#!/usr/bin/python3

quiz = [116, 66, 85, 81, 93, 120, 81, 83, 91]

for i in range(len(quiz)):
    quiz[i] ^= 0x30
print(quiz)
quiz = ''.join([chr(_) for _ in quiz])
print(quiz)
answer = input()

if answer == quiz:
    print("Welcome Hackers :)")
else:
    print("No No :/")