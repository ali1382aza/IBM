# meta classes
متا کلاس‌ها به شما اجازه می‌دهند تا نحوه تعریف و رفتار کلاس‌ها را کنترل کنید.متا کلاس در پایتون، کلاسی است که برای ایجاد کلاس‌های دیگر استفاده می‌شود. به عبارت دیگر، متا کلاس‌ها "کلاس‌های کلاس‌ها" هستند. هر چیزی در پایتون یک شیء است، از جمله کلاس‌ها. وقتی یک کلاس جدید در پایتون تعریف می‌شود، یک نمونه از متا کلاس ایجاد می‌شود. به صورت پیش‌فرض، متا کلاس پایه در پایتون type است.

```py
class MyClass:
    pass

print(type(MyClass))  

```

```py
<class 'type'>
```
---
#### ساختار متا کلاس ها:
برای ایجاد یک متا کلاس سفارشی، باید از type ارث‌بری انجام داد و متد \__new__ یا 
\__init__ را بازنویسی کرد.

```py
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(cls, name, bases, dct)

```

متد \__new__ مسئول ایجاد و مقداردهی اولیه کلاس جدید است. این متد چهار پارامتر اصلی دریافت می‌کند:

cls: خود متا کلاس

name: نام کلاس جدید

bases: تاپل کلاس‌های پایه (ارث‌بری)

dct: دیکشنری شامل ویژگی‌ها و متدهای کلاس
___
### استفاده از متاکلاس ها:

برای استفاده از یک متا کلاس، باید پارامتر metaclass را در تعریف کلاس مشخص کنید.

```py
class MyClass(metaclass=Meta):
    pass
```
___
### کاربردهای متا کلاس‌ها:

1)اضافه کردن ویژگی‌ها و متدهای خاص:

متا کلاس‌ها می‌توانند به صورت خودکار ویژگی‌ها یا متدهای خاصی را به تمامی کلاس‌های ساخته شده اضافه کنند. این ویژگی به خصوص زمانی مفید است که نیاز دارید تا ویژگی‌ها یا متدهای مشترکی در چندین کلاس داشته باشید.

```py
class AutoAddMethodsMeta(type):
    def __new__(cls, name, bases, dct):
        dct['auto_method'] = lambda self: 'This is an auto method'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AutoAddMethodsMeta):
    pass

instance = MyClass()
print(instance.auto_method())
```

```py
This is an auto method
```
___

2)اعمال محدودیت‌ها و اعتبارسنجی:

متا کلاس‌ها می‌توانند قواعد و محدودیت‌هایی را برای کلاس‌ها اعمال کنند و مطمئن شوند که کلاس‌های ایجاد شده با آن قواعد همخوانی دارند. به عنوان مثال، می‌توانیم مطمئن شویم که تمامی نام‌های ویژگی‌ها با حروف کوچک نوشته شده باشند.

```py
class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:
            if not attr_name.startswith('__') and not attr_name.islower():
                raise ValueError(f'Attribute {attr_name} must be lowercase')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=ValidateMeta):
    def my_method(self):
        pass
```
در این مثال، متا کلاس ValidateMeta مطمئن می‌شود که تمام نام‌های ویژگی‌ها و متدها با حروف کوچک شروع می‌شوند. اگر این شرایط نقض شود، یک خطای ValueError برگردانده می‌شود.
___
3)پیاده‌سازی الگوهای طراحی (Design Patterns):

متاکلاس‌ها می‌توانند برای پیاده‌سازی الگوهای طراحی مانند Singleton، Factory، و دیگر الگوهای پیچیده استفاده شوند.

```py
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

obj1 = SingletonClass(1)
obj2 = SingletonClass(2)
print(obj1.value)
print(obj2.value) 
print(obj1 is obj2) 
```

```py
1
1
True
```
___
4)افزودن ویژگی‌های خودکار به کلاس‌ها:

متاکلاس‌ها می‌توانند به طور خودکار ویژگی‌ها و متدهای جدید به کلاس‌ها اضافه کنند.

```py
class AutoAttributeMeta(type):
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        new_class.auto_attribute = "This is an auto attribute"
        return new_class

class MyClass(metaclass=AutoAttributeMeta):
    pass

obj = MyClass()
print(obj.auto_attribute)
```

```py
This is an auto attribute
```
___