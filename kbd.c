#include <stdio.h>
#include <wiringPi.h>

#define PIN 31

int main()
{
  wiringPiSetupPhys();
  int counts[1024];
  int idx = 0;
  int count;
  int i;

  pinMode(PIN, INPUT);

  while(1)
  {
    for(count = 0; digitalRead(PIN); count++) {
      if(count > 100000) {
        if (idx != 0) {
          for (i = 0; i < idx; i++) {
            printf("%d ", counts[i]);
          }
          printf("\n");
        }
	count = 0;
        idx = 0;
      }
    }

    counts[idx++] = count;

    for(count = 0; !digitalRead(PIN); count++);
    counts[idx++] = count;

    if(idx > 1000) idx = 0;
  }
}
