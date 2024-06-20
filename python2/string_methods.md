#  متد های رشته در پایتون
1)capitalize()

اولین کاراکتر متن را به کاراکتر بزرگ تبدیل می کند
```py
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

```

```py
Hello, and welcome to my world.
```
___
2)casefold()

تمامی کاراکتر های متن را به کاراکتر موچک تبدیل می کند.
```py
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)
```

```py
hello, and welcome to my world!
```
___
3)center()

یک رشته ای که در مرکز قرار گرفته را برایمان برمی گرداند
```py
txt = "banana"

x = txt.center(20)

print(x)
```

```py

       banana
```
___
4)count()

تعداد دفعاتی که یک مقدار مشخص در یک رشته به وقوع پیوسته را برمیگرداند.
```py
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
```

```py
2
```
___
5)encode()

این متد رشته مورد نظر را رمز گذاری می کند.
```py
txt = "My name is Ståle"

x = txt.encode()

print(x)

```

```py
b'My name is St\xc3\xe5le'
```
___
6)endswith()

در صورتی که رشته با چیزی که ما در داخل پارانتز تعیین کردیم تمام شود True را برمی گرداند.
```py
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
```

```py
True
```
___
7)expandtabs()

سایز تب را در داخل رشته تنظیم می کند.
```py
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)
```

```py
H e l l o
```
___
8)find()

به دنبال مقدار خاص تعیین شده می گردد و جایگاه اولین جایی که آن مقدار در آنجا وجود دارد را برمی گرداند. 
```py
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
```

```py
7
```
___
9)format()


```py
#شاخص نام گذاری شده:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#شاخص شماره گذاری شده:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#شاخص های بدون شماره گذاری:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

```

```py
My name is John, I'm 36
My name is John, I'm 36
My name is John, I'm 36
```
___
10)index()

به دنبال مقدار خاصی که تعیین کردیم می گردد و یکی بیشتر از شاخصه جایی که در آن چایان یافته را بر می گرداند.
```py
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

```

```py
7
```
___
11)isalnum()

در صورتی که تمام مقادیر داخل رشته فقط الفبایی یا اعداد صفر تا 9 باشند True را بر می گرداند و در صورت وجود کاراکتری غیر اینها False.
```py
txt = "Company12"

x = txt.isalnum()

print(x)
```

```py
True
```
___
12)isalpha()

در صورتی که تمام کاراکتر های داخل رشته الفبایی باشند مقدار True را بر می گرداند وبرعکس.
```py
txt = "CompanyX"

x = txt.isalpha()

print(x)
```

```py
True
```
___
13)isascii()

در صورتی که تمام کاراکترهای داخل رشته کاراکتر اسکی باشند مقدار True را برمی گرداند و برعکس.
```py
txt = "Company123"

x = txt.isascii()

print(x)
```

```py
True
```
___
14)isdecimal()

در صورتی که تمام کاراکتر های داخل رشته بر مبنای ده یا 0تا 9 باشند مقدار True را برمی گرداند و در غیر اینصورت مقدار False.
```py
txt = "1234"

x = txt.isdecimal()

print(x)
```

```py
True
```
___
15)isdigit()

در صورتی که تمام کاراکتر ها رقم باشند True را بر می گرداند ودر غیر این صورت False
```py
txt = "50800"

x = txt.isdigit()

print(x)

```

```py
True
```
___
16)isidentifier()

در صورتی که رشته فقط دارای حروف الفبا و اعداد 0 تا 9 و زیر خط باشد True را بر می گرداند و در غیر این صورت False 
```py
txt = "Demo"

x = txt.isidentifier()

print(x)
```

```py
True
```
___
17)islower()

در صورتی که رشته فقط دارای حروف کوچک باشد مقدار True را برمی گداند و در غیر این صورت False
```py
txt = "hello world!"

x = txt.islower()

print(x)
```

```py
True
```
___
18)isnumeric()

در صورتی که تمام مقادیر موجود در رشته عددی باشند مقدار True را بر می گرداند و در غیر اینصورت false
```py
txt = "565543"

x = txt.isnumeric()

print(x)
```

```py
True
```
___
19)isprintable()

در صورتی که تمام کاراکتر های رشته قابل پرینت باشد به صورت مستقیم مقدار  True را برمی گرداند و در غیر اینصورت مقدار False
```py
txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)
```

```py
False
```
___
20)isspace()

در صورتی که کاراکتر های داخل رشته فقط دارای اسپیس باشند مقدار  True را برمی گرداند و در غیر اینصورت مقدار False
```py
txt = "   "

x = txt.isspace()

print(x)
```

```py
True
```
___
21)istitle()

در صورتی که رشته از قوانین تایتل یا موضوع طبعیت کند مقدار  True را برمی گرداند و در غیر اینصورت مقدار False
```py
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
```

```py
False
True
True
True
```
___
22)isupper()

در صورتی که تمامی کاراکتر های موجود در رشته از حروف بزرگ تشکیل شده باشند مقدار  True را برمی گرداند و در غیر اینصورت مقدار False
```py
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

```

```py
True
```
___
23)join()

مجموعه ای از تکرار پذیر هارا دریافت می کند و آنها را همراه کاراکتر خاص وارد شده داخل یک تکرار پذیر قرار می دهد و بر می گرداند
```py
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
```

```py
#John#Peter#Vicky
```
___
24)ljust()

همراه خود رشته خاص فاصله ای مشخص می کنیم و در سمت راست آن رشته آن مقدار معین را از تعداد کاراکتر های رشته کسر می کند و بقیه اش را اسپیس یا فاصله قرار می دهد.
```py
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")
```

```py
banana              is my favorite fruit.
```
___
25)lower()

تمامی کاراکتر های موجود در رشته را به حروف کوچک تبدیل می کند.
```py
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)
```

```py
hello my friends
```
___
26)lstrip()

از سمت چپ هر گونه کاراکتری که داخل پرانتز تعریف شده را حذف می کند.
```py
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
```

```py
banana
```
___
27)maketrans()

در این تابع رشته مورد نظر ما با تغییراتی که در نظر داریم برگردانده و ترجمه می شود
```py
txt = "Hello Sam!"

mytable = str.maketrans("S", "P")

print(txt.translate(mytable))
```

```py
Hello Pam!
```
___
28)partition()

دنبال رشته مورد نظر داخل پرانتز در رشته مورد نظر می گردد و تاپلی با 3 قسمت قبل معادل،معادل و پس از معادل را می دهد. 
```py
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

```

```py
('I could eat ', 'bananas', ' all day')
```
___
29)replace()

یک رشته ای که یک عبارتش بلا عبارت دیگری جایگزین شده است را تحویل می دهد.
```py
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)
```

```py
I like apples
```
___
30)rfind()

از سمت راست عبارتی که داخل پرانتز تعیین شده است را پیدا می کند و جایگاه آنرا برمی گرداند
```py
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)
```

```py
12
```
___
31)rindex()

از سمت راست به دنبال عبارتی که داخل پرانتز مشخص شده است می گردد و جایگاه آنرا بر می گرداند
```py
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)
```

```py
12
```
___
32)rjust()

از سمت راست به طور پیش فرض به طبق اندازه تعیین شده غیر از کاراکتر اصلی فاصله قرار می دهد
```py
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
```

```py
              banana is my favorite fruit.
```
___
33)rpartition()

به دنبال رشته مشخص شده می گردد و رشته اصلی را به سه قسمت قبل رشته ،خود رشته و بعد رشته در یک تاپل برمی گرداند
```py
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)
```

```py
('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
```
___
34)rsplit()

از سمت راست رشته مشخص شده را تقسیم بندی می کند ودر صورتی که مقدار ماکسیمم در ورودی دوم تاپل مشخص نشود با split() تفاوتی ندارد
```py
txt = "apple, banana, cherry"

x = txt.rsplit(", ", 1)

print(x)
```

```py
['apple, banana', 'cherry']
```
___
35)rstrip()

فضا های خالی از سمت راست را حذف می کند و رشته را بر میگرداند
```py
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")
```

```py
of all fruits     banana is my favorite
```
___
36)split()

رشته مورد نظر را بر اساس کاراکتر مشخص شده جدا سازی می کند و به صورت پیش فرض با فاصله جدا سازی میکند (در صورت تعیین نکردن)
```py
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
```

```py
['hello', 'my name is Peter', 'I am 26 years old']
```
___
37)splitlines()

رشته مشخص شده را بر اساس پایان خط(\n )جدا سازی می کند
```py
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
```

```py
['Thank you for the music', 'Welcome to the jungle']
```
___
38)startswith()

در صورتی که رشته مورد نظر با مقدار مورد نظر ما شروع شود مقدار True را بر می گرداند و در غیر اینصورت False.
```py
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

```

```py
True
```
___
39)strip()

هرگونه کاراکتر مشخص شده داخل پرانتز از داخل رشته مورد نظر ما حذف می گردد.
```py
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
```

```py
banana
```
___
40)swapcase()

این تابع حروف بزرگ داخل رشته را به حروف کوچک و حروف کوچک را به حروف بزرگ تبدیل می کند.
```py
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
```

```py
hELLO mY nAME iS peter
```
___
41)title()

هر حرف هر کلمه داخل رشته را به حرف بزرگ تبدیل می کند.  
```py
txt = "Welcome to my world"

x = txt.title()

print(x)
```

```py
Welcome To My World
```
___
42)translate()

یک رشته را که کاراکترش با کاراکتری دیگر تعویض شده را برمی گرداند
```py
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))
```

```py
Hello Pam!
```
___
43)upper()

تمامی حروف یک رشته را به حروف بزرگ تبدیل می کند.
```py
txt = "Hello my friends"

x = txt.upper()

print(x)
```

```py
HELLO MY FRIENDS
```
___
44)zfill()

تازمانی که تعداد کاراکتر های رشته به تعداد مشخص شده داخل پارانتز برسند از سمت راست رشته با 0 پر می شود 
```py
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
```

```py
00000hello
welcome to the jungle
000010.000
```
___
