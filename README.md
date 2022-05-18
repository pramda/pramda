# Pramda

Pramda helps you implement functional programming in Python

I didn't have a good functional programming tool like Ramda.js, so I made it.

[ [Pypi](https://pypi.org/project/pramda/) ]

### Install

```sh
$ pip install pramda
```

### How to use

add

```py
add(1, 2) # 3
add(1)(2) # 3
```

adjust

```py
adjust(0, add(2), [1]) # 3
adjust(2, add(10), [4, 3, 2, 1]) # 12
```

all

```py
is_one = lambda x: x == 1

all(is_one, [1, 1, 1, 1])   # True
all(is_one, [1, 1, 1, 2])   # False
all(is_one)([2, 1, 1, 1])   # False
all(is_one)([2, 2, 2, 2])   # False
all(is_one)([1, 1, 1, 1])   # True
```

any

```py
any(is_one, [1, 1, 1, 1])   # True
any(is_one, [1, 1, 1, 2])   # True
any(is_one)([2, 1, 1, 1])   # True
any(is_one)([2, 2, 2, 2])   # False
any(is_one)([1.1, 1, 1, 1]) # True
```

curry

```py
@curry
def example(a, b):
  return f'{a} equals {b}'

example('1', 'one') # 1 equals one
example('2')('two') # 2 equals two
```

gt

```py
gt(1, 2)   # False
gt(2, 2)   # False
gt(2.1, 2) # True
gt(3, 2)   # True
```

gte

```py
gte(1, 2)   # False
gte(2, 2)   # True
gte(2.1, 2) # True
gte(3, 2)   # True
```

lt

```py
lt(1, 2)   # True
lt(2, 2)   # False
lt(2.1, 2) # False
lt(3, 2)   # False
```

lte

```py
lte(1, 2)   # True
lte(2, 2)   # True
lte(2.1, 2) # False
lte(3, 2)   # False
```

map

```py
multiplication = lambda x: x * 2
map(multiplication, [4, 2, 3]) # [8, 4, 6]
map(multiplication)([4, 2, 3]) # [8, 4, 6]
```

pipe

```py
inc = lambda x: x + 1

pipe(inc, inc, inc, inc, inc)(1) # 6
```

reduce

```py
reduce(add, [1, 2, 3])                 # 6
reduce(concat_string, ["a", "b", "c"]) # "abc"
```

cond

```py
@curry
equal(a, b):
  return a == b

test = cond(
  [equal(1),   lambda _: 'a'],
  [equal(10),  lambda _: 'b'],
  [equal(50),  lambda _: 'c'],
  [equal(100), lambda _: 'd'],
)

test(1)   # "a"
test(10)  # "b"
test(50)  # "c"
test(100) # "d"
```
