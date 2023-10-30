n = [1,2,3,4,5,6,7,8,9,10]
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
print('#' * 50)
r = [1,2,3,4,5,1,2,3]
print(r.index(3))
if 5 in r:
  print('exist')
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
print('#' * 50)
s = 'My name is Mike. Hi Mike.'
to_split = s.split(' ')
print(to_split)
x = ' '.join(to_split)
print(x)
print('#' * 50)
x = [1,2,3,4,5]
y = x.copy()
y[0] = 100
print(f'y = {y}')
print(f'x = {x}')
print('#' * 50)
num_tuple = (10, 20)
x, y = num_tuple
print(x, y)
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)
print('#' * 50)
fruits = {
  'apple': 100,
  'banana': 200,
  'orange': 300
}
print(fruits['apple'])
print('#' * 50)
a = {1,2,2,3,4,4,5,6}
print(a)
b = {2,3,3,6,7}
print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)