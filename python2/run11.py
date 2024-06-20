import re

# الگوی یک ایمیل
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# یک متن تست
text = "ایمیل‌های موردنظر در این متن foo@example.com و bar@example.com هستند."

# جستجوی ایمیل‌ها با استفاده از عبارت با قاعده
emails = re.findall(email_pattern, text)

# چاپ ایمیل‌های یافته شده
print(emails)
