#include <stdio.h>

int main(){
    int size1,size2,g=0,i=0;
    scanf("%d %d",&size1,&size2);
    int numbers1[size1],numbers2[size2];
    for(int i=0;i<size1;i++){
        scanf("%d",&numbers1[i]);
    }
    for(int i=0;i<size2;i++){
        scanf("%d",&numbers2[i]);
    }
    while(g<size1 && i<size2){
        if(numbers1[g]<numbers2[i]){
            printf("%d",numbers1[g]);
            g++;
        }
        if(numbers1[g]>numbers2[i]){
            printf("%d",numbers2[i]);
            i++;
        }
        if(numbers1[g]==numbers2[i]){
            printf("%d",numbers1[g]);
            printf("%d",numbers1[g]);
            i++;
            g++;
        }
    }
    while(g<size1){
        printf("%d",numbers1[g]);
        g++;
    }
    while(i<size2){
        printf("%d",numbers2[i]);
        i++;
    }
}