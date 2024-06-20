#include <stdio.h>

int main(){
    int v,e;

    scanf("%d",&v);
    scanf("%d",&e);
    int mojaverat_matrix[v][v],a,b;
    for(int i=0;i<v;i++){
        for(int j=0;j<v;j++){
            mojaverat_matrix[i][j]=0;
        }
    }

    for(int i=0;i<e;i++){
        scanf("%d",&a);
        scanf("%d",&b);
        mojaverat_matrix[a-1][b-1]=1;
    }

    for(int i=0;i<v;i++){
        for(int j=0;j<v;j++){
            printf("%d",mojaverat_matrix[i][j]);
        }
        printf("\n");
    }
}