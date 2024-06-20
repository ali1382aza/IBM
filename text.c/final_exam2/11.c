#include <stdio.h>

int main(){
    int sh,va,ph,as,sa,ga;
    scanf("%d",&sh);
    scanf("%d",&va);
    scanf("%d",&ph);
    scanf("%d",&as);
    scanf("%d",&sa);
    scanf("%d",&ga);
    if(sh>1){
        printf("%d",(1-sh));
    }
    else if(sh<1){
        printf("1");
    }
    else{
        printf("0");
    }


    if(va>1){
        printf("%d",(1-sh));
    }
    else if(va<1){
        printf("1");
    }
    else{
        printf("0");
    }


    if(ph>2){
        printf("%d",(2-sh));
    }
    else if(ph==1){
        printf("1");
    }
    else{
        printf("0");
    }
}