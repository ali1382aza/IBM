#include <stdio.h>
#include <math.h>

int main(){
    int x,d,r,result=0,tavan=0;
    scanf("%d",&x);
    scanf("%d",&d);
    while(x!=0){
        r=x%d;
        result+=r*(pow(10,tavan));
        x/=d;
        tavan++;
    }
    printf("%d",result);
}