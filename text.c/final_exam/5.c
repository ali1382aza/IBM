#include <stdio.h>

int main(){
    int i, j;
for (i = 0; i <= 3; i = i + 1){
for (j = 0; j <= 4; j = j + 1){
if ( (i + 1 == j) ) {
printf("+");
}
else {
printf("o");
}
}
printf("\n");
}
}

