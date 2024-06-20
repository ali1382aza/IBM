#include <stdio.h>

int main(){
    int a,b,c;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    if (a+b+c!=180){
        printf("No");
    }
    else if(a==0 || b==0 || c==0){
        printf("No");
    }
    else if(a>=180 || b>=180 || c>=180){
        printf("No");
    }
    else if((a+b)>=180){
        printf("No");
    }
    else if ((a+c)>=180){
        printf("No");
    }
    else if ((b+c)>=180){
        printf("No");
    }
    else {
        printf("Yes");
    }
}