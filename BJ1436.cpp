#include <iostream>
#include <string>

using namespace std;

int main(){
    int array[10000] = {0};
    int userInput = 0;
    int i = 0;
    int index = 0;
    int arrIndex = 0;

    while (array[9999] == 0)
    {
        string i_ = to_string(i);

        if (i_.find("666") != std::string::npos) {
            array[arrIndex] = i;
            arrIndex += 1;
            index = 0;
        }

        i++;
    }
    
    cin >> userInput;
    cout << array[userInput - 1];
    
    return 0;
}