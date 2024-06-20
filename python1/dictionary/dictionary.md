# متد های دیکشنری
1)clear()

تمام عناصر را از دیکشنری پاک می کند و یک دیکشنری خالی تحویل می دهد.

```py
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
```

```py
{}
```
___
2)copy()

یک کپی از دیکشنری را برای ما برمی گرداند.

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)
```

```py
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```
___

3)fromkeys()

این متد دیکشنری با مقادیر تعیین شده داخل  پرانتز(کلید ها در متغیر اولی قرار دارند)
و مقادیر در متغیر دوم قرار دارند.

```py
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)


print(thisdict)

```

```py
{'key1': 0, 'key2': 0, 'key3': 0}
```

مثال دوم:

```py
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
```

```py
{'key1': None, 'key2': None, 'key3': None}
```
___

4)get()

با استفاده از این متد می توان مقدار کلید مشخص شده داخل پرانتز را دریافت کرد.

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
```

```py
Mustang
```

مثال دوم که برای زمانی است که تلاش می کنیم مقدار کلیدی را دریافت کنیم که در دیکشنری وجود ندارد.

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)
```

```py
15000
```
___

5)items()

جفت کلید ها و مقادیر را در یک تاپل و مجموع تاپل ها را در داخل یک لیست قرار می دهد.


```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
```

```py
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

مثال دوم:


```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)

```

```py
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
```
___

6)keys()

کلید های یک دیکشنری را در داخل لیست قرار می دهد و لیست را در داخل یک تاپل قرار می دهد.

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)
```

```py
dict_keys(['brand', 'model', 'year'])
```
___

7)pop()

این متد در داخل پرانتز یک کلید را می گیرد و آنرا از دیکشنری مشخص شده حذف می کند 
```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)
```

```py
{'brand': 'Ford', 'year': 1964}
```
___

8)popitem()

آخرین کلید و مقدار در داخل دیکشنری را از دیکشنری مورد نظر حذف می کند.

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)
```

```py
{'brand': 'Ford', 'model': 'Mustang'}
```

مثال دوم:کلید و مقدار حذف شده را هم می توانیم بگیریم.

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)
```

```py
('year', 1964)
```
___

9)setdefault()

در این متد در صورتیکه مقدار کلید وارد شده داخل پرانتز موجود نباشد با تعیین مقدار پیش فرض داخل پرانتز از خطا جلوگیری می کنیم و این مقدار را برای کلید ناموجود دریافت می کنیم


```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
```

```py
Mustang
```

مثال دوم:

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

print(x)
```

```py
White
```
___

10)update()

این متد یک آیتم را دریافت کرده و آنرا داخل دیکشنری مورد نظر می کند.


```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)
```

```py
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
```
___

11)values()

یک لیستی از مقادیر در داخل دیکشنری را برایمان برمی گرداند

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

```

```py
dict_values(['Ford', 'Mustang', 1964])
```

مثال دوم :

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)
```

```py
dict_values(['Ford', 'Mustang', 2018])
```
___
# عملگر های دیکشنری
1)عملگر 
[ ]
:

با استفاده از این عملگر می توان به مقدار کلید در داخل این عملگر دسترسی پیدا کرد.

```py
my_dict = {'ali':1,'reza':2,'amir':3}

print(my_dict[ali])
```

```py
1
```
___
2)عملگر in:

```py
my_dict = {'ali':1,'reza':2,'amir':3}

print('ali' in my_dict)
```

```py
True
```
___
3)عملگر not in:

```py
my_dict = {'ali':1,'reza':2,'amir':3}

print('ali' not in my_dict)
```

```py
False
```
___