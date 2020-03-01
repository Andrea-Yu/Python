```python
print("hi~")
```

    hi~
    


```python
print("Hello world!", end = '')
print("ya!")
```

    Hello world!ya!
    


```python
print("Hello", "World!")
```

    Hello World!
    


```python
var1 = 0b10; var2 = 0o10; var3 = 0x10
print(var1, var2, var3)
```

    2 8 16
    


```python
var1 = 1e-5; var2 = 6.7e15; var3 = 6.7e16; var4 = -1.8
print(var1, var2, var3, var4)
```

    1e-05 6700000000000000.0 6.7e+16 -1.8
    


```python
var1 = 3+5.3j; var2 = complex(3.4e5, 7.8)
print(var1, type(var1))
print(var2, type(var2))
```

    (3+5.3j) <class 'complex'>
    (340000+7.8j) <class 'complex'>
    


```python
i_love_u = True
u_love_me = False
print(i_love_u, type(i_love_u))
print(u_love_me, type(u_love_me))
```

    True <class 'bool'>
    False <class 'bool'>
    


```python
-10 // -3
```




    3




```python
10 % -3
```




    -2




```python
-10%3
```




    2




```python
10%3
```




    1




```python
10 and 20+5
0 and 20+5
```




    0




```python
str1 = '''first line
second line
third line'''
print(str1)
```

    first line
    second line
    third line
    


```python
x = [1,2,3,4,5,6,7]
print(x[0:6])
```

    [1, 2, 3, 4, 5, 6]
    


```python
t = (1, [1, 2, 3], 4)
t[1]
```




    [1, 2, 3]




```python
t[1][2] = 4
```


```python
t
```




    (1, [1, 2, 4], 4)




```python
t[0] = 3
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-724a2335dedd> in <module>
    ----> 1 t[0] = 3
    

    TypeError: 'tuple' object does not support item assignment



```python
s1 = {1, 2, 3, 4}
s2 = {2}
s1 - s2
```




    {1, 3, 4}




```python
s2 - s1
```




    set()




```python
s2 = {2, 5, 6}
s1 - s2
```




    {1, 3, 4}




```python
s2 - s1
```




    {5, 6}




```python
# %c 格式化字符及其ASCII码
print("%c" % "A")
print("%c" % 65)
```

    A
    A
    


```python
# %s 格式化字符串
print("%s" % "Hello World!")

# %d 格式化无符号十六进制数
print("%x" % 20)
# 在十六进制前面显示‘0x’或者‘0X’（取决于x/X）
print("%#x" % 20)

# 格式化浮点数
print("%f" % 3.14)
# 指定小数点后的精度 
# m.n (m-total-当原本位数小于指定宽度时适用)
print("%2.2f" % 3.14)
print("%10.2f" % 3.14)
# 左对齐 - 
print("%-10.2f" % 3.14)
# 添加+号
print("%+10.2f" % 3.14)
print("%+10.2f" % -3.14)
# 用*从后面的元组中读取宽度或精度
pi = 3.1415926
print("pi = %.*f" % (5, pi))

# 自动化格式化浮点数的小数或科学计数法的表现方法
print("%g" % 314000000)
print("%g" % 3140)
```

    Hello World!
    14
    0x14
    3.140000
    3.14
          3.14
    3.14      
         +3.14
         -3.14
    pi = 3.14159
    3.14e+08
    3140
    


```python
# 元组填充
print("I like %s and can eat %.2f kg." % ("orange", 1.5))
```

    I like orange and can eat 1.50 kg.
    


```python
# 使用字典来对应填充
print("I like %(fruit_name)s and can eat %(weight).2f kg." % {"fruit_name" : "orange", "weight" : 1.5})
```

    I like orange and can eat 1.50 kg.
    


```python
x = 8
calc = "5*x+9"
eval(calc)
```




    49




```python
sdfjhsrgjdjbvidjhgsijfdcjhvdvcjhsldru = 1
kjchxvihdsgfdiuyervbshkfwiefodgvjcvosifsfhdv = 2
dusifydufgjvpofiusdgfsoijsgdbfisduyvgskifjfsdfoiweo = 3

result = sdfjhsrgjdjbvidjhgsijfdcjhvdvcjhsldru +\
kjchxvihdsgfdiuyervbshkfwiefodgvjcvosifsfhdv +\
dusifydufgjvpofiusdgfsoijsgdbfisduyvgskifjfsdfoiweo

print(result)
```

    6
    


```python
for i in range(1,10):
    print(i)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    


```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
[x*y for x in list1 for y in list2]
```




    [4, 5, 6, 8, 10, 12, 12, 15, 18]




```python
def func_example(a, b = 0, c = "hhhh"):
    "我是函数说明我是函数说明我是函数说明我是函数说明"
    a.append("new")
    b += 1
    return a, b, c
```


```python
func_example.__doc__
```




    '我是函数说明我是函数说明我是函数说明我是函数说明'




```python
number = 5

def func1():
    print(number)
    
func1()
print(number)
```

    5
    5
    


```python
number = 5

def func2():
    number = 3
    print(number)
    
func2()
print(number)
```

    3
    5
    


```python
number = 5

def func3():
    global number
    number = 3
    print(number)
    
func3()
print(number)
```

    3
    3
    


```python
# 写文件
with open("text.txt", "wt") as out_file:
    out_file.write("我写进来了\n看见了吧！")
```


```python
# 读文件
with open("text.txt", "rt") as in_file:
    text = in_file.read()
    
print(text)
```

    我写进来了
    看见了吧！
    


```python
def except_function():
    try:
        # 故意除零
        10 / 0
    except:
        print("error: divide 0")
    else:
        # 正常情况
        print("一切正常")
        pass
    finally:
        # 无论是否发生异常都将执行
        print("finally必须被执行，无论是否发生异常")
```


```python
except_function()
```

    error: divide 0
    finally必须被执行，无论是否发生异常
    


```python
dir(1)
```




    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']




```python

```
