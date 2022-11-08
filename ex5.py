a = int(input('a-> '))
b = int(input('b-> '))

action = input('Enter your action(+ - avg * ): ')

if action == '+':
    res = a + b
    print("Ur result" + " " + str(res))
elif action == '-':
    res = a - b
    print("Ur result" + " " + str(res))
elif action == 'avg':
    res = (a + b) / 2
    print("Ur result" + " " + str(res))
elif action == '*':
    res = a * b
    print("Ur result" + " " + str(res))
else:
    print("Entered wrong number/sign")
print("Good Luck!")