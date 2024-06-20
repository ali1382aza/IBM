#include <stdio.h>

int main(){
    float a, b;
    char c;
    scanf("%f",&a);
    scanf("%f\n",&b);
    scanf("%c",&c);
    if(c==43){
        printf("%.2f",a+b);
    }
    if(c==45){
        printf("%.2f",a-b);
    }
    if(c==47){
        if(b==0){
            printf("0");
        }
        else{
            printf("%.2f",a/b);
        }
    }
    if(c==42){
        printf("%.2f",a*b);
    }
    if(c!=43 && c!=45 &&  c!=47 && c!=42){
        printf("0");
    }
}