#include <stdio.h>


// تعریف تابع برای چک کردن تطابق پرانتز
int isBalanced(char expression[]){
    char stack[100];
    int top = -1;
    for (int i=0; expression[i]; i++) {
        if (expression[i]=='(' || expression[i]=='{' || expression[i]=='['){
            // اگر پرانتز باز مشاهده شد، آن را در استک قرار می‌دهیم
            stack[++top] = expression[i];
        }
        else if (expression[i]==')' || expression[i]=='}' || expression[i]==']'){
            // اگر پرانتز بسته مشاهده شد
            // اگر استک خالی باشد یا پرانتز متناظر با از بالای استک نباشد، تطابق وجود ندارد
            if (top==-1 || (expression[i]==')' && stack[top]!='(') || (expression[i]=='}' && stack[top]!='{') || (expression[i]==']' && stack[top]!='[')){
                return 0; // ناتطابق
            }
            else{
                top--; // حذف پرانتز از استک به عنوان تطابق پیدا شده
            }
        }
    }
    // بررسی اینکه آیا استک باقیمانده است یا خالی شده است
    return (top == -1);
}

int main() {
    char expression[100];
    gets(expression);
    if (isBalanced(expression)) {
        printf("correct");
    } else {
        printf("wrong");
    }
    return 0;
}
