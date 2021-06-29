#include <iostream>
#include <string>
using namespace std;

int main() {
    int userNum = 0;
    int count = 0;
    string a = 0;
    string b = 0;
    string result = "";
    int same = 0;

    cout << "횟수를 입력하세요";
    cin >> userNum;

    string userCon[userNum];

    for(int i=0; i<userNum; i++){
        cout << "문자를 입력하세요";
        cin >> userCon[i];
    }

    for(int j=0; j<userNum; j++){
        for(int i=0; i<userCon[j].length(); i++){
            a = userCon[j].at(i);
            b = userCon[j+1].at(i);
            if (a == b){
                same = 1;
            } else{
                same = 0;
                break;
            }
        }
        if (same == 1){
            result += a;
        } else if (same == 0){
            result += "?";
        }
    }

    return 0;
}
