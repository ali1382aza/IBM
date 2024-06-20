# متد های متعلق به file در پایتون
1)close()

این تابع فایل را می بندد و دسترسی به آن را قطع می کند.
```py
f = open("demofile.txt", "r")

print(f.read())

f.close()
```

```py
#فایل پس از خوانده شدن بسته می شود
```
___
2)seek()

موقعیت خواندن فایل را عوض می کند 
```py
f = open("demofile.txt", "r")
f.seek(4)
print(f.readline())
```

```py
#فایل از شاخص چهارم به بعد خوانده می شود
```
___
3)fileno()

جریان توصیف گر فایل را برمی گرداند.
```py
f = open("demofile.txt", "r")

print(f.fileno())
```

```py
3
```
___
4)flush()

این تابع حافظه حایل یا بافر را پاک می کند.
```py
f = open("myfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")
```

```py
#خالی
```
___
5)isatty()

مقدار True را برمی گرداند در صورتی که جریان فایل در ارتباط باشد
```py
f = open("demofile.txt", "r")

print(f.isatty())
```

```py
False
```
___
6)read()

محتوای یک فایل را می خواند و ارائه می دهد(در صورت تعیین سایز  تا آن مقدار را می خواند)
```py
f = open("demofile.txt", "r")

print(f.read())
```

```py
#ارائه مقدار خوانده شده
```
___
7)readable()

در صورتی که فایل قابل خواندن باشد مقدار True را برمی گرداند و در غیر اینصورت مقدار False.
```py
f = open("demofile.txt", "r")

print(f.readable())
```

```py
True
```
___
8)readline()

یک خط مشخص شده (داخل پارانتز)از فایل را بر می گرداند.
```py
f = open("demofile.txt", "r")
print(f.readline())
```

```py
#خط یکم از فایل را به ما می دهد
```
___
9)seekable()

به ما امکان تغییر موقعیت در فایل را نشان می دهد و مقدار درست یا غلط را بر می گرداند
```py
f = open("demofile.txt", "r")

print(f.seekable())
```

```py
True
```
___
10)tell()

موقعیت فعلی جریان فایل را برمی گرداند.
```py
f = open("demofile.txt", "r")
print(f.tell())
```

```py
0
```
___
11)truncate()

این متد قایل را به اندازه بایت داده شده کوتاه می کند.
```py
f = open("demofile2.txt", "a")
f.truncate(20)
f.close()


f = open("demofile2.txt", "r")
print(f.read())

```

```py
#محتوای فایل به اندازه 20 بایت در می آید و چاپ می شود.
```
___
12)writable()

در صورتی که فایل قابل خواندن باشد مقدار True را برمی گرداند و در غیر اینصورت False.
```py
f = open("demofile.txt", "a")
print(f.writable())
```

```py
True
```
___
13)write()

یک رشته را روی فایل مورد نظر می نویسد و اضافه می کند.
```py
f = open("demofile2.txt", "a")
f.write("See you soon!")
f.close()


f = open("demofile2.txt", "r")
print(f.read())
```

```py
#فایل مورد نظر همراه رشته جدید چاپ می گردد.
```
___
14)writelines()

این متد آیتم های داخل یک لیست را به یک فایل اضافه می کند.
```py
f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()

f = open("demofile3.txt", "r")
print(f.read())
```

```py
#فایل همراه با مطلب اضافه شده لیست مورد نظر چاپ می شود.
```
___