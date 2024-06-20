#include <stdio.h>

int main(){
    int row1, column1, column2;

    scanf("%d", &row1);
    scanf("%d", &column1);
    scanf("%d", &column2);

    int matrix1[row1][column1], matrix2[column1][column2], result[row1][column2];
    
    for(int i=0; i<row1; i++){
        for(int j=0; j<column1; j++){
            scanf("%d", &matrix1[i][j]);
        }
    }

    for(int i=0; i<column1; i++){
        for(int j=0; j<column2; j++){
            scanf("%d", &matrix2[i][j]);
        }
    }
     for(int i=0;i<row1;i++){
        for(int j=0;j<column1;j++){
            result[i][j]=0;
            for(int h=0;h<column1;h++){
                result[i][j]+=matrix1 [i][h] * matrix2[h][j];
            }
        }
    }

    for(int i=0;i<row1;i++){
        for(int j=0;j<column2;j++){
            printf("%d\t",result[i][j]);
        }
        printf("\n");
    }
}

