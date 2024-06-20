# متد های لیست ها
1) append()

برای اضافه کردن یک عنصر به انتهای لیست استفاده میگردد. 

مثال:

![m](./Screenshot%202024-03-07%20085844.png) ![m](./Screenshot%202024-03-07%20085854.png)

![m](./Screenshot%202024-03-07%20085917.png)
![m](./Screenshot%202024-03-07%20085928.png)

___
2) copy()

برای کپی کم عمق و سطحی از یک لیست استفاده می گردد.

![alt text](<Screenshot 2024-03-07 090817.png>)![alt text](<Screenshot 2024-03-07 090834.png>)
___
3) clear()

این متد برای حذف همه اعضای یک لیست استفاده می گردد.

![alt text](<Screenshot 2024-03-07 092021.png>)![alt text](<Screenshot 2024-03-07 092034.png>)
___
4) count()

این متد برای شمارش عناصر لیست به کار میرود.

![alt text](<Screenshot 2024-03-07 092120.png>)![alt text](<Screenshot 2024-03-07 092132.png>)

![alt text](<Screenshot 2024-03-07 092239.png>)![alt text](<Screenshot 2024-03-07 092248.png>)
____
5) extend()

هر کدام از اعضای یک تکرار پذیر(iterable)را به انتهای لیست اضافه می کند.
![alt text](<Screenshot 2024-03-07 092323.png>)![alt text](<Screenshot 2024-03-07 092335.png>)

![alt text](<Screenshot 2024-03-07 092404.png>)![alt text](<Screenshot 2024-03-07 092411.png>)

___
6) index()

کم ترین شاخص و جایگاه عنصر مدر نظر در داخل پرانتز را برمیگرداند.

![alt text](<Screenshot 2024-03-07 093235.png>)
![alt text](<Screenshot 2024-03-07 093246.png>)
___
7) insert()

یک عنصر معین را در یک شاخص معین در یک لیست درج می کند.

![alt text](<Screenshot 2024-03-07 093235-1.png>)
![alt text](<Screenshot 2024-03-07 093457.png>)


___
8) pop()

این متد با مشخص کردن شاخص یا جایگاه در داخل پرانتز،آن عضو را در داخل لیست حذف میکند .در صورتی که شاخص یا ایندکس مشخص نگردد عنصر آخر از لیست را حذف می کند.

![alt text](<Screenshot 2024-03-07 093548.png>)
![alt text](<Screenshot 2024-03-07 093558.png>)

![alt text](<Screenshot 2024-03-07 093618.png>)
![alt text](<Screenshot 2024-03-07 093626.png>)
___
9) remove()

شی داده شده در داخل پرانتز را از لیست حذف می کند

![alt text](<Screenshot 2024-03-07 104928.png>)![alt text](<Screenshot 2024-03-07 104938.png>)
___
10) reverse()

اشیای لیست را در جای خود برعکس می کند.

![alt text](<Screenshot 2024-03-07 105046.png>)![alt text](<Screenshot 2024-03-07 105056.png>)
___
11) sort()

فهرست را به ترتیب صعودی،نزولی یاتعریف شده توسط کاربر مرتب می 
کند

![alt text](<Screenshot 2024-03-07 105147.png>)![alt text](<Screenshot 2024-03-07 105157.png>)

![alt text](<Screenshot 2024-03-07 105235.png>)
![alt text](<Screenshot 2024-03-07 105245.png>)

![alt text](<Screenshot 2024-03-07 105313.png>)
![alt text](<Screenshot 2024-03-07 105325.png>)
____
12) min()

حداقل و کمترین مقدار داخل عناصر لیست را محاسبه می کند
```py
numbers = [23,25,65,21,98]
print(min(numbers))

```
```py
21
```
___
13) max()

بیشترین مقدار تمام عناصر ز لیست را محاسبه می کند

```py
var1 = 4
var2 = 8
var3 = 2

max_val = max(var1, var2, var3)
print(max_val)

```
```py
8
```

```py
var1 = "geeks"
var2 = "for"
var3 = "geek"

max_val = max(var1, var2, var3)
print(max_val)

```
```py
geeks
```
___
# عملگر های لیست
1)عملگر جمع
(+):
این عملگر برای اتصال دو لیست به یکدیگر به کار می رود
```py
list1 =[1,2,3]
list2 =[4,5]
sum = list1 + list2
print(result)
```

```py
[1,2,3,4,5]
```
___
2)عملگر ضرب (*):
این عملگر برای تکرار یک تاپل در یک لیست استفاده می شود.

```py
list1 =[1,2]
result =list1 * 2
print(result)
```

```py
[1,2,1,2,1,2]
```
___
3)عملگر in:
این عملگربرای بررسی وجود یک عنصر در یک لیست استفاده می شود و در صورت وجود، مقدار True را بر می گرداند.

```py
list1 =[1,2,3]
print(2 in list1)
```

```py
True
```
___