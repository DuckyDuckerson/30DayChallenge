#include <stdio.h>
#include <unistd.h>
#include <string.h>


void printing(int index, const char *message, float delay) {
  if (index < strlen(message)) {
    putchar(message[index]);
    fflush(stdout);
    usleep((int)(delay * 1000000)); // convert delay to microseconds
    printing(index + 1, message, delay);
  }
}


void print_message(const char *message, int speed, int newline) {
  float speed_map[6] = {0, 0.2, 0.05, 0.01, 0.007, 0.003};
  float delay = speed_map[speed];
    
    
  printing(0, message, delay);
    
  if (newline == 1) {
    putchar('\n');
  }
}
