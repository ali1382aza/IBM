# متد های مجموعه یا ست
1)add()

برای اضافه کردن به یک مجموعه به کار میرود.
```py
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```

```py
{'orange', 'apple', 'banana', 'cherry'}
```
___
2)clear()

تمام عناصر یک ست را پاک می کند.

```py
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
```

```py
set()
```
___
3)copy()

یک کپی از ست را برمی گرداند.

```py
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

```

```py
{'apple', 'banana', 'cherry'}
```
___
4)difference()

تفاوت های بین دو یا چند مجموعه را به  صورت یک مجموعه بر میگرداند یعنی موارد تکراری را از مجموعه اول حذف می کند.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)
```

```py
{'banana', 'cherry'}
```
___
5)difference_update()

موارد موجود در مجموعه را که در مجموعه مشخص دیگری نیز گنجانده شده اند، حذف می کند.
تفاوت این متد با قبلی این است که اولی خود یک مجموعه می سازد اما در دومی اعمال بر روی خود مجموعه موجود اجرا می شود

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)
```

```py
{'banana', 'cherry'}
```
___
6)discard()

مورد مشخص شده را حذف می کند.

```py
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
```

```py
{'cherry', 'apple'}
```
___
7)intersection()

آیتم هایی را برمی گرداند که در هردو مجموعه موجود باشد.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)
```

```py
{'apple'}
```
___
8)intersection_update()

آیتم هایی که در هر دو مجموعه موجود نیست را از مجموعه مورد نظر حذف می کند

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) 

print(x)
```

```py
{'apple'}
```
___
9)issubset()

در صورتی که اعضای مجموعه اول در مجموعه دوم وجود داشته باشند True 
را برمی گرداند در غیر اینصورت مقدار False
را برمی گرداند  
```py
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) 

print(z)
```

```py
True
```
___
10)issuperset()

در صورتی که تمام اعضای مجموعه دوم در اعضای مجموعه اول موجود باشد مقدار 
True 
را بر می گرداند در غیر اینصورت 
False
را بر می گرداند

```py
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y) 

print(z)
```

```py
True
```
___
11)pop()

یک آیتم را به طور تصادفی از مجموعه حذف می کند

```py
fruits = {"apple", "banana", "cherry"}

fruits.pop() 

print(fruits)
```

```py
{'banana', 'cherry'}
```
___
12)remove()

یک عنصر خاص را از مجموعه حذف می کند.

```py
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana") 

print(fruits)
```

```py
{'apple', 'cherry'}
```
___
13)symmetric_difference()

مجموعه ای را بر می گرداند که شامل تمام عناصر دو مجموعه به غیر از عناصری که در هر دو مجموعه وجود دارند است

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)
```

```py
{'google', 'banana', 'cherry', 'microsoft'}
```
___
14)symmetric_difference_update()

تمام عناصری که در مجموعه اول و دوم موجود اند به غیر عناصر موجود در هر دو مجموعه را در مجموعه اول قرار می دهد.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) 

print(x)
```

```py
{'banana', 'microsoft', 'cherry', 'google'}
```
___
15)union()

اجتماع دو مجموعه را محاسبه می کند و در مجموعه جدید قرار می دهد یعنی جمع هر دو مجموعه منهای یک عنصر تکراری برای جلوگیری از تکرار آن

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y) 

print(z)

```

```py
{'cherry', 'google', 'apple', 'banana', 'microsoft'}
```
___
16)update()

تمام عناصر مجموعه ای که در داخل پرانتز است را در داخل محموعه اول قرار می دهد
```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) 

print(x)
```

```py
{'banana', 'microsoft', 'google', 'cherry', 'apple'}
```
___
17)isdisjoint()

اگر هیچ آیتمی در مجموعه اول در مجموعه دوم موجود نباشد True را برمی گرداند
در غیر اینصورت False 
را برمی گرداند.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) 

print(z)
```

```py
True
```
___
# عملگر های ست یا مجموعه
1)عملگر | یا عملگر اتحاد:
این عملگر برای اتحاد دو مجموعه به کار می رود و تمام عناصر هر دو مجموعه را در داخل یک مجموعه جدید قرار می دهد

```py
set1 = {1,2,3}
set2 = {4,5}

result = set1|set2

print(result)
```

```py
{1,2,3,4,5}
```
___
2)عملگر & یا عملگر اشتراک:

```py
set1 = {1,2,3}
set2 = {3,4,5}

result = set1 & set2

print(result)
```

```py
{3}
```
___
3)عملگر - یا تفاضل:

این عملگر برای یافتن تفاضل دو مجموعهبه کار می رود یعنی اشتراک دو مجموعه را از مجموعه مورد نظر حذف می کند.

```py
set1 = {1,2,3}
set2 = {3,4,5}

result = set1 - set2
```

```py
{1,2}
```
___