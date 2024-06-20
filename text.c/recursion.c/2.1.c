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

int amal(int a,int x,int n){
    int sum=1,sumasl=0;
    for(int i=n;i>=0;i--){
    sum*=tarkib(n,i);
    sum*=pow(x,i);
    sum*=pow(a,(n-i));
    sumasl+=sum;
    sum=1;    
    }
    return sumasl;
}

int main(){
    int a,x,n,result;
    scanf("%d %d %d",&a,&x,&n);
    result=amal(a,x,n);
    printf("%d",result);

}