#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;

    cout << "Input a String" << "\n";
    cin >> s;

    bool isPalindrom = true;
    int n = s.length();

    for(int i=0;i < n/2;i++){
        // String Reverse Operation
        if (s[i] != s[n-1-i]){
            isPalindrom = false;
        }
    }

    string output = (isPalindrom == true) ? "Palindrom" : "Not Palindrom";
    cout << output << "\n";
}