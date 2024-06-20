#include <stdio.h>
#include <math.h>

int main(){
    int x,d=0,c,f,result;
    scanf("%d",&x);
    while(x>0){
        d*=10;
        d+=(x%10);
        
        x/=10;
    }
    c=d%10;
    f=((d%1000)/100);
    result=((d/1000)*1000)+(100*c)+(((d/10)%10)*10)+f+15;
    printf("%d",result);
}