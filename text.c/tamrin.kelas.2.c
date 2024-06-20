#include <stdio.h>
#include <math.h>
int main(){
    int n,x,c,m,b,s,l,f,k;
    scanf("%d", &n);
    for(b=0; b<n; b+=1){
        scanf("%d", &x);
        for(c=1; 0==0; c+=1){
            m=pow(10,c);
            if(m>x){
                break;
            }
        }
        s=0;
        for(k=0; k<=c; k+=2){
            m=pow(10,k);
            l=pow(10,k+1);
            f=pow(10,c-k-1);
            s+=(x%l-x%m)*f;
            }
    }
    printf("%d", s);
}