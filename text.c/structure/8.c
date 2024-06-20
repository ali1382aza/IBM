#include <stdio.h>
#include <string.h>
#include <math.h>


int con(int n,int g){
    if(n>0){
        return(pow(10,g)*(n%2)+con(n/2,g+1));
    }
    else{
        return 0;
    }
}

int main(){
    int bin;
    scanf("%d",&bin);
    int result=con(bin,0);
    printf("%d",result);
}