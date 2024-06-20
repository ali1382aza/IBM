#include <stdio.h>
#include <math.h>

int be10(int n,int mabna){
    int mabna10=0;
    int tavan=0;

    while(n!=0){
        int remainder=n%10;
        mabna10+=remainder*pow(mabna,tavan);
        n/=10;
        tavan++;
    }
    return mabna10;
}
int az10(int n,int mabna){
    int convertedn=0;
    int tavan=0;

    while(n!=0){
        int remainder=n%mabna;
        convertedn+=remainder*pow(10,tavan);
        n/=mabna;
        tavan++;
    }
    return convertedn;
}
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    int mabna10=be10(a,b);
    int result=az10(mabna10,c);

    printf("%d",result);

    return 0;
}