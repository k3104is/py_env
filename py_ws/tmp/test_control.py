y = [1,2,3]
x = 1
if x in y:
  print('in')
if 100 not in y:
  print('not in')

is_ok = True

if is_ok:
  print('hello')

if not is_ok:
  print('hello')

is_empty = None
# print(help(is_empty))
# isはオブジェクト同士が同じもの(メモリ上のまったく同じ値)かどうかを判別
if is_empty is None:  
  print('none!!!')

print('#' * 50)

count = 0
while count < 5:
  print(count)
  count += 1
else:
  print('Done')

count = 0
while True:
  if count >= 5:
    break
  print(count)
  count += 1

count = 0
while count < 5:
  if count == 1:
    break
  print(count)
  count += 1
else:
  print('Done')

while True:
  word = input('Enter:')
  if word == 'ok':
    break
  print('next')