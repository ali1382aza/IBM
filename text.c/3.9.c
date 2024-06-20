#include <stdio.h>

int main(){
    int a ,b ,c ,d;
    scanf("%d %d %d",&a,&b,&c);
    int x1=a%10 , x2=b%10 , x3=c%10;
    if(x1>x2 && x1>x3){
        d=a;
    }
    else if(x2>x1 && x2>x3){
        d=b;
    }
    else if(x3>x1 && x3>x2){
        d=c;
    }
    else if(x1==x2 && x1>x3){
        if(a>b){
            d=a;
        }
        else{
            d=b;
        }
    }
    else if(x1==x3 && x1>x2){
        if(a>c){
            d=a;
        }
        else{
            d=c;
        }
    }
    else if(x2==x3 && x2>x1){
        if(b>c){
            d=b;
        }
        else{
            d=c;
        }
    }
    else if(x1==x2 && x1==x3){
        if(a>=b && a>=c){
            d=a;
        }
        else if(b>=a && b>=c){
            d=b;
        }
        else{
            d=c;
        }
    }
    printf("%d",d);
}