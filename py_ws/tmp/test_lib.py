print(globals())

ranking = {
  'A': 100,
  'B': 85,
  'C': 92
}

print('\n' + '#' * 10 + '\n')

for key in ranking:
  print(key)

print(sorted(ranking))
print(sorted(ranking, key=ranking.get))
print(sorted(ranking, key=ranking.get, reverse=True))
print('\n' + '#' * 10 + '\n')

s = "fdjsafiewafjdsaeiwfdafke"

d = {}
for c in s:
  if c not in d:
    d[c] = 0
  d[c] += 1
print(d)

d = {}
for c in s:
  d.setdefault(c, 0)
  d[c] += 1
print(d)

from collections import defaultdict
d = defaultdict(int)
for c in s:
  d[c] += 1
print(d)
print('\n' + '#' * 10 + '\n')

from termcolor import colored
print(colored('test', 'red'))
# print(help(colored))

print('\n' + '#' * 10 + '\n')
