#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - sleep
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: 0 or 1
 */

int main(void)
{
	pid_t zompie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zompie = fork();
		if (!zompie)
			return (1);
		printf("Zombie process created, PID: %d\n", zompie);
	}
	infinite_while();
	return (0);
}

