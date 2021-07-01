#include <iostream>
#include <string>
using namespace std;

int main() {
    int userNum = 0;
    string userStr = "";
    string result = "";
    int a = 0;
    string first = "";
    string second = "";
    string tmp = "";

    cin >> userNum;

    string stringList[userNum];

    for(int i = 0; i < userNum; i++){
        cin >> userStr;
        if (userNum == 1){
            cout << userStr;
            break;
        }
        stringList[i] = userStr;
    }


#include <iostream>
#include <string>
    using namespace std;

    int main() {
        int userNum = 0;
        string userStr = "";
        string result = "";
        int a = 0;
        string first = "";
        string second = "";
        string tmp = "";

        cin >> userNum;

        string stringList[userNum];

        for(int i = 0; i < userNum; i++){
            cin >> userStr;
            if (userNum == 1){
                cout << userStr;
                break;
            }
            stringList[i] = userStr;
        }



        for(int j = 0; j < stringList[0].length(); j++){
            first = stringList[0].at(j);
            second = stringList[1].at(j);

            if (first == second){
                result += first;
            } else if (first != second){
                result += "?";
            }
        }

        a = stringList[0].length();

        for(int i = 1; i < userNum; i++){
            for(int j = 0; j < a; j++){
                first = result.at(j);
                second = stringList[i].at(j);

                if (first == second){
                    tmp += first;
                } else if (first != second){
                    tmp += "?";
                }
            }

            result = tmp;
            tmp = "";
        }

        cout << result;

        return 0;

    }




    for(int j = 0; j < stringList[0].length(); j++){
        first = stringList[0].at(j);
        second = stringList[1].at(j);

        if (first == second){
            result += first;
        } else if (first != second){
            result += "?";
        }
    }

    a = stringList[0].length();

    for(int i = 1; i < userNum; i++){
        for(int j = 0; j < a; j++){
           first = result.at(j);
           second = stringList[i].at(j);

            if (first == second){
                tmp += first;
            } else if (first != second){
                tmp += "?";
            }
        }

        result = tmp;
        tmp = "";
    }

    cout << result;

    return 0;

    }



