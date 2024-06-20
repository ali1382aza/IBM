#include <stdio.h>

int main() {
    char araye[100];
    int size;
    scanf("%d",&size);
    scanf("%s",araye);


    for (int i = 0; i < size - 1; i++) {
        if (araye[i] == araye[i + 1]) {
            for (int j = i; j < size - 1; j++) {
                araye[j] = araye[j + 2];
            }
            size = size - 2;
            i=-1;
        }
    }


    printf("%s",araye);

    return 0;
}
