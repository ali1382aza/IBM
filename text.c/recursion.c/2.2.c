#include <stdio.h>
#include <math.h>

int fac(int x){
    if(x>0){
        return x*fac(x-1);
    }
    else{
        return 1;
    }
}

int tarkib(int x,int y){
    return (fac(x)/(fac(y)*fac(x-y)));
}

int amal(int a,int x,int n,int d){
    if(d>=0){
        return tarkib(n,d)*pow(x,d)*pow(a,(n-d))+amal(a,x,n,d-1);
    }
    else{
        return 0;
    }
}
int main(){
    int a,x,n,result,d;
    scanf("%d %d %d",&a,&x,&n);
    d=n;
    result=amal(a,x,n,d);
    printf("%d",result);
}