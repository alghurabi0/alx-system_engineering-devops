#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("fork");
			exit(1);
		}
		if (child_pid == 0)
		{
			// This is the child process
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while(); // Keep the program running

	return (0);
}
