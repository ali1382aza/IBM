#include <stdio.h>
#include <math.h>
int main(){
    int i,x,sum=0,c;
    scanf("%d",&i);
    c=i;
    while(i!=0){
        x=i%10;
        i=i/10;
        sum+=pow(x,3);
    }
    if(c==sum){
        printf("Yes");
    }
    else{
        printf("NO");
    }
}
