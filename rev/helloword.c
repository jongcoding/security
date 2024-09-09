/*
    File: hello-world.cpp
    Build opts:
      - /MT -> Library Static Linking
      - /DYNAMICBASE:NO -> Disable ASLR
      - /od -> Disable Optimization
*/

#include <Windows.h>
#include <stdio.h>

char* str;
int main() {
  int delay = 1000;
  Sleep(delay);  // 1000ms(1초)를 대기합니다.
  str = (char*)"Hello, world!\n";
  printf(str);
  return 0;
}
