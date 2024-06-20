# توابع built_in پایتون
1)abs()

قدر مطلق یک مقدار را برایمان برمی گرداند
```py
x = abs(-7.25)
print(x)
```

```py
7.25
```
___
2)all()

در صورتی که تمامی مقدار یک ایتریبل یا تکرار پذیر True باشد True را بر می گرداند و برعکس 
```py
mylist = [True, True, True]
x = all(mylist)
print(x)
```

```py
True
```
___
3)any()

در صورتی که مقداری در ایتریبل وجود دداشته باشد که True است مقدار True را برمی گرداند و برعکس
```py
mylist = [False, True, False]
x = any(mylist)
print(x)
```

```py
True
```
___
4)ascii()

کاراکتر هایی که اسکی نیستند را حذف و شکل اسکی آنها را جایگزین می کند
```py
x = ascii("My name is Ståle")
print(x)
```

```py
'My name is St\e5le'

```
___
5)bin()

شکل باینری متغیر را برایمان برمی گرداند
```py
x = bin(36)
print(x)

# نتیجه همیشه با پیشوند  (0b)
```

```py
0b100100

```
___
6)bool()

مقدار بولین یک آبجکت را برمی گرداند
```py
x = bool(1)
print(x)
```

```py
True
```
___
7)bytearray()

مقدار آرایه بایتی یک شی را برمی گرداند
```py
x = bytearray(4)
print(x)
```

```py
bytearray(b'\x00\x00\x00\x00')
```
___
8)bytes()

آبجکت بایت یک آبجت را برمی گرداند
```py
x = bytes(4)
print(x)
```

```py
b'\x00\x00\x00\x00' 
```
___
9)callable()

در صورتی که تابع مورد نظر قابل فراخوانی و صدار کردن باشد مقدار True را برمی گرداند و برعکس
```py
def x():
  a = 5

print(callable(x))
```

```py
True
```
___
10)chr()

این تابع کاراکتر مقداری که بایونیکد خاصی مشخص می شود را برمیگرداند
```py
x = chr(97)

print(x)
```

```py
a
```
___
11)classmethod()

یک متد را به کلاس متد تبدیل می کند

___
12)compile()

یک متن را به عنوان یک کد کامپیال می کند و آنرا اجرا می کند
```py
x = compile('print(55)', 'test', 'eval')
exec(x)
```

```py
55
```
___
13)complex()

با گرفتن دو ورودی عدد مختلط بر می گرداند
```py
x = complex(3, 5)
print(x)
```

```py
(3+5j)
```
___
14)delattr()

یک صفت (ویژگی یا متد ) را از یک آبجکت حذف می کند.
```py
class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')

# دیگر آبجکت انسانی با ویژگی سن باقی نخواهد ماند
```
___
15)dict()

یک دیکشنری حاوی اطلاعات
```py
x = dict(name = "John", age = 36, country = "Norway")

print(x)
```

```py
{'name': 'John', 'age': 36, 'country': 'Norway'}
```
___
16)dir()

تمامی متد ها و ویژگی های آبجکت را برمی گرداند  
```py
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))
```

```py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'country', 'name']
```
___
17)divmod()

یک تاپل حاوی خارج قسمت و باقی مانده را برمی گرداند 
```py
x = divmod(5, 2)

print(x)
```

```py
(2, 1)
```
___
18)enumerate()

تاپل را به یک آبجکت قابل شمارش تبدیل می کند.
```py
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))
```

```py
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

```
___
19)eval()

عبارت داخلش را ارزیابی می کند و در صورت کد قابل اجرا آن را اجرا می کند
```py
x = 'print(55)'
eval(x)
```

```py
55
```
___
20)exec()

یک بلوک و مجموعه از کد را انجام می دهد و برخلاف eval تعداد کد زیادی را در داخل خود می پذیرد
```py
x = 'name = "John"\nprint(name)'
exec(x)
```

```py
John
```
___
21)filter()

یک آبجکت قابل شمارش دریافت می کند و آنرا بر اساس تابع داده شده فیلتر و مرتب می کند
```py
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
```

```py
18
24
32
```
___
22)float()

عدد مورد نظر داخل پرانتز را تبدیل به اعشاری می کند 
```py
x = float(3)

print(x)

```

```py
3.0
```
___
23)format()

برای نشان دادن عبارت داخل فرمت به فرم مشخص شده داخل فرمت به کار می رود
```py
x = format(0.5, '%')

print(x)
```

```py
50.000000%
```
___
24)frozenset()

یک لیست را به یک آبجکت غیرقابل تغییر تبدیل می کند که مانند ست یا مجموعه است اما غیر قابل تغییر
```py
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

```

```py
frozenset({'cherry', 'banana', 'apple'})
```
___
26)getattr()

مقدار یک ویژگی مشخص شده داخل یک آبجکت را بر می گرداند
```py
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')

print(x)
```

```py
36
```
___
27)globals()

این تابع صفحه جهانی علامت هارا برمی گرداند این صفحه علامت شامل اطلاعات ضروری درباره برنامه فعلی است
```py
x = globals()
print(x)
```

```py
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x02A8C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}
```

```py
x = globals()
print(x["__file__"])
```

```py
demo_ref_globals2.py
```
___
28)hasattr()

چک می کند که آیا یک ویژگی داخل یک آبجکت وجود داره یا خیر که در صورت درست بودن True را بر می گرداند و برعکس
```py
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')

print(x)
```

```py
True
```
___
29)hash()

مقدار hash یک تابع را بر می گرداند

___
30)help()

سیستم داخلی کمک را انجام می دهد

___
31)hex()

یک مقدار را دریافت می کند و آنرا به هگزا دسیمال تبدیل می کند
```py
x = hex(255)
print(x)
```

```py
0xff
```
___
32)id()

آدرس حافظه را که آبجکت در آن ذخیره شده است را بر می گرداند
```py
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
```

```py
52492087
```
___
33)input()

به کاربر اجازه وارد کردن مقدار را می دهد
```py
print("Enter your name:")
x = input()
print("Hello, " + x)
```

```py
Enter your name:
```
___
34)int()

این تابع مقدار مشخصی را به عدد صحیح تبدیل می کند
```py
x = int(3.5)

print(x)
```

```py
3
```
___
35)isinstance()

آبجکت داده شده مثالی از تایپ های داده شده باشد مقدار True را بر می گرداند و برعکس.
```py
x = isinstance("Hello", (str, float, int, str, list, dict, tuple))

print(x)

```

```py
True
```
___
36)issubclass()

در صورتی که یک کلاس یک زیرکلاس برای کلاس دیگر باشد مقدار True را برمی گرداند
```py
class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)

print(x)
```

```py
True
```
___
37)iter()

یک آبجکتی با نوع ایتریتور یا شمارگر را بر می گرداند
```py
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
```

```py
apple
banana
cherry
```
___
38)len()

طول یک آبجکت را بر می گرداند
```py
mylist = ["apple", "orange", "cherry"]

x = len(mylist)

print(x)
```

```py
3
```
___
39)list()

این تابع از یک قابل شمارش یک لیست می سازد 
```py
x = list(('apple', 'banana', 'cherry'))

print(x)
```

```py
['apple', 'banana', 'cherry']
```
___
40)locals()

صفحه نماد های محلی را نمایش می دهد.
```py
x = locals()
print(x)
```

```py
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0327C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}

```
___
41)map()

این تابع یک تابع را دریافت و سپس یک قابل شمارش را دریافت می کند و اعمال تابع را روی قابل شمارش اجرا می کند
```py
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#برای تبدیل مپ به متنی خواندنی باید آنرا به لیست تبدیل کرد
print(list(x))
```

```py
<map object at 0x056D44F0>
[5, 6, 6]
```
___
42)max()

بزرگترین مقدار ییک تکرار پذیر را بر می گرداند.
```py
x = max(5, 10)

print(x)
```

```py
10
```
___
43)memoryview()	

یک آبجکت مموری ویو برمی گرداند.
```py
x = memoryview(b"Hello")

print(x)
```

```py
<memory at 0x03348FA0>
```
___
44)min()

کوچکترین مقدار را در داخل یک تکرار پذیر بر می گرداند.
```py
x = min(5, 10)

print(x)
```

```py
5
```
___
45)next()

آیتم بعدی را در داخل یک تکرار پذیر بر می گرداند
```py
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)
```

```py
apple
banana
cherry
```
___
46)object()

یک آبجکت خالی را می سازد و تحویل می دهد
```py
x = object()

print(dir(x))
```

```py
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

```
___
47)oct()

یک عدد صحیح دریافت می کند و آنرا به سیستم مبنای 8 تبدیل می کند.
```py
x = oct(12)

print(x)
```

```py
0o14
```
___
48)open()

یک فایل را باز می کند که نام فایل و مد و روشی که برای آن فایل را باز می کند نیز دریافت می کند.
```py
f = open("demofile.txt", "r")

print(f.read())
```

```py
#محتوای داخل فایلی که آدرس آن داده شده است چاپ می کند
```
___
49)ord()

مقدار یونیکد کاراکتری را که دریافت می کند را بر می گرداند
```py
x = ord("h")

print(x)
```

```py
104
```
___
50)pow()

دو عدد داخل پرانتز دریافت می کند و عدد اولی را به توان عدد دوم می رساند.
```py
x = pow(4, 3)

print(x)
```

```py
64
```
___
51)print()

یک آبجکتی را که به استرینگ یا رشته تبدیل شده است را چاپ می کند
```py
print("Hello", "how are you?")
```

```py
Hello how are you?
```
___
52)property()

ویژگی را دریافت می کند،حذف می کند و یا تنظیم می کند. 

___
53)range()

یک دنباله ای از اعداد بر می گرداند که از صفر شروع شده و تا یکی قبل عدد تعریف شده ادامه پیدا می کند.
```py
x = range(6)

for n in x:
  print(n)
```

```py
0
1
2
3
4
5
```
___
54)repr()

یک نسخه قایل خواندن از آبجکت مورد نظر را بر می گرداند.

___
55)reversed()

یک دنباله ای که تکرار پذیر می باشد را می گیرد و آنرا معکوس می کند.
```py
alph = ["a", "b", "c", "d"]

ralph = reversed(alph)

for x in ralph:
  print(x)

```

```py
d
c
b
a
```
___
56)round()

یک عدد را به مقداری که تعریف می کنیم و تا آن تعداد رقم گرد می کند.
```py
x = round(5.76543, 2)
print(x)
```

```py
5.77
```
___
57)set()

یک آبجکت جدید که از نوع ست یا مجموعه است را بر می گرداندو همچنین باید تکرار پذیر در داخل خود دریافت کند.
```py
x = set(("apple", "banana", "cherry"))

print(x)
```

```py
{'banana', 'cherry', 'apple'}
```
___
58)setattr()

مقدار نوعی ویژگی مشخص شده در نوعی آبجکت مشخص را تنظیم و تایین می کند
```py
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

# اکنون ویژگی سن 40 خواهد بود

x = getattr(Person, 'age')

print(x)
```

```py
40
```
___
59)slice()

یک آبجکتی به نام اسلایس برمی گرداند(کهشیوه تقسیم بندی آبجکت در آن مشخص می شود)

```py
a = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(2)

print(a[x])
```

```py
('a', 'b')
```
___
60)sorted()

یک لیستی از یک تکرار پذیر برمی گرداند که مرتب شده می باشد.
```py
a = ("b", "g", "a", "d", "f", "c", "h", "e")

x = sorted(a)

print(x)
```

```py
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```
___

61)staticmethod()

یک متد را به یک متدایستا یا راکد تبدیل می کند.

___
62)str()

یک آبجکت مشخص را تبدیل به رشته می کند.
```py
x = str(3.5)

print(x)
```

```py
3.5
```
___
63)sum()

موارد داخل یک تکرار پذیر را جمع می کند و برمی گرداند.
```py
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)
```

```py
15
```
___
64)super()

یک آبجکتی را برمی گرداند که کلاس والدین آنرا بر می گرداند.
```py
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()
```

```py
Hello, and welcome!
```
___
65)tuple()

این تابع یک آبجکت به نام تاپل از آبجکت قبلی درست می کند.
```py
x = tuple(("apple", "banana", "cherry"))

print(x)

```

```py
('banana', 'cherry', 'apple')
```
___
66)type()

نوع و گونه آبجکت را بر می گرداند.
```py
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x)
print(y)
print(z)
```

```py
<class 'tuple'>
<class 'str'>
<class 'int'>
```
___
67)vars()

ویژگی های__dict__ یک آبجکت را برمی گرداند 
```py
class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)

print(x)
```

```py
{'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'norway', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
```
___
68)zip()

یک ایتریتور که خود نیز شامل دو یا چند ایتریتور دیگر است را برمی گرداند
```py
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#برای چاپ کردن زیپ نیاز به تبدیل آن به تاپل داریم

print(tuple(x))
```

```py
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
```
___
