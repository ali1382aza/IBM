#include <stdio.h>

int digit(int n,int position){
    int d=0;
    while((d)!= position){
        n/=10;
        d++;
    }
    return n%10;
}

int main(){
    int n,g=0,adad,position,result;
    scanf("%d",&n);
    scanf("%d",&position);
    adad=n;
    while(adad!=0){
        adad/=10;
        g++;
    }
    position=(g-position);
    result=digit(n,position);
    printf("%d",result);
}