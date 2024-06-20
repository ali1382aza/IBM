#include <stdio.h>

int main() {
    int s1, s2;
    scanf("%d",&s1);
    scanf("%d",&s2);
    int araye1[s1],size_kol = s1 + s2 , araye_tarkib[size_kol],araye2[s2];

    for(int i=0;i<s1;i++){
        scanf("%d",&araye1[i]);
    }
    for(int i=0;i<s2;i++){
        scanf("%d",&araye2[i]);
    }


    int i = 0, j = 0, k = 0;

    while (i < s1 && j < s2) {
        if (araye1[i] <= araye2[j]) {
            araye_tarkib[k] = araye1[i];
            i++;
        } else {
            araye_tarkib[k] = araye2[j];
            j++;
        }
        k++;
    }

    while (i < s1) {
        araye_tarkib[k] = araye1[i];
        i++;
        k++;
    }

    while (j < s2) {
        araye_tarkib[k] = araye2[j];
        j++;
        k++;
    }

    for (int m = 0; m < size_kol; m++) {
        printf("%d ", araye_tarkib[m]);
    }
}
