#include <stdio.h>

int main(){
    int x=1 ,b=1 ,sum=0,y;
    scanf("%d",&y);
    while(b<=y){
        printf("%d",x);
        if(b<=(y-1)){
            printf("+");
        }
        b++ ;
        sum+=x ;
        x=10*x+1;
    }
    printf("=%d",sum);
}