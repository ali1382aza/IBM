#include <stdio.h>

int main(){

    int matris[3][4],sum=0;

    for(int i=0;i<4;i++){
        for(int j=0;j<3;j++){
            scanf("%d",&matris[i][j]);
        }
    }
    for(int i=0;i<4;i++){
        for(int j=0;j<3;j++){
            sum+=matris[i][j];
        }
        printf("jam satr%d is %d\n",(i+1),sum);
        sum=0;
    }

}