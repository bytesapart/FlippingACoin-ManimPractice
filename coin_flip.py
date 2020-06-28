import random
outcomes = []
for i in range(6000000):
    outcomes.append(random.choice(['H', 'T']))
print(outcomes.count('H'))
print(outcomes.count('T'))
