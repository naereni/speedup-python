#include <iostream>

using namespace std;

int main()
{
    int digitals[] = {95642, 93197, 87725, 39170, 51477, 62826, 63613, 24655, 92459, 89632, 13};

    for (int i = 0; i < 10000; i++) {
        bool flag = true;
        for (int j = 0; j < 10 - (i + 1); j++) { 
            if (digitals[j] > digitals[j + 1]) {
                flag = false;
                swap (digitals[j], digitals[j + 1]);
            }
        }
        if (flag) {
            break;
        }
    }
}
