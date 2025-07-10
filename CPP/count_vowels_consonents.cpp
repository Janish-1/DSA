#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;

    cout << "Count Vowels and Consonants" << "\n";
    cin >> s;

    int n = s.length();
    int vowels = 0;
    int consonants = 0;
    int invalid = 0;

    for(int i=0; i<n; i++){
        char temp = tolower(s[i]);
        if( (temp > 'a') && (temp < 'z')){
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
                vowels++;
            } else {
                consonants++;
            }
        } else {
            invalid++;
        }
    }

    cout << "Vowels Count: " << vowels << "\n";
    cout << "Consonants Count: " << consonants << "\n";
    cout << "Invalid Count: " << invalid << "\n";
}