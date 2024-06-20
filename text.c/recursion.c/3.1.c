#include <stdio.h>

int fac(int x){
    if(x>0){
        return x*fac(x-1);
    }
    else{
        return 1;
    }
}
int tarkib(int n,int k){
    return (fac(n)/(fac(k)*fac(n-k)));
}
int main(){
    int n,result;
    scanf("%d",&n);
    for (int r=0;r<n;r++){
        for(int c=0;c<=r;c++){
            result=tarkib(r,c);
            printf("%d ",result);
        }
        printf("\n");
    }
}