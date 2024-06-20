#include <stdio.h>

int main(){
    int n,c;
    scanf("%d",&n);
    int x[n];
    for(int i=0;i<n;i++){
        scanf("%d",&x[i]);
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(x[i]>x[j]){
                c=x[i];
                x[i]=x[j];
                x[j]=c;
            }
        }
    }
    for(int i=(n-1);i>=0;i--){
        printf("%d ",x[i]);
    }
}