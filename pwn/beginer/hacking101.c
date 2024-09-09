#include <stdio.h>

void fun (int x, int y)
{
	int z;	
	char buf[100];
	
	z = x;
	read (0, buf, y);

	printf ("x is %d\n", x);
	//printf (“z is %d\n”, z);
}

int main (int argc, char* argv[])
{
	int a, b;
	a = 30;
	b = 300;

	fun (a,b);
}