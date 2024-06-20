#include <stdio.h>

int main(){
    int number;
    scanf("%d",&number);
    int number2=number;
    int reverse=0,remainder;
    while(number!=0){
    remainder=number%10;
    reverse=reverse*10+remainder;
    number=number/10;
    }
    if(reverse==number2){
        printf("YES");
    }
    else{
        printf("NO");
    }
}