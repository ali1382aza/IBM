#include <stdio.h>

int F1 (int a, int b);
int F2 (int a, int b);
int main() {
int a = 1, b = 2, c = 3;

c = F1 (a, b);
printf ("%d %d %d\n", a, b, c);
b = F2 (a, c);
printf ("%d %d %d\n", a, b, c);
a = F2 ( F1 (a, c), b);
printf ("%d %d %d\n", a, b, c);
b = F2 (a, c) / F1 (b, c);
printf ("%d %d %d\n", a, b, F1 (a, b) );
}
int F1 (int a, int b) {
return (a + b + 3);
}
int F2 (int a, int b){
return ((a + b) % 3);
}
