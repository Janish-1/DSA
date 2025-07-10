#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;

    cout << "Input a String for Reverse Operation" << "\n";
    cin >> s;

    int n = s.length();
    
    cout << "Original Word: " << s << "\n";
    cout << "Word Length: " << n << "\n";

    // Doing 2 Characters at a time
    for(int i = 0;i < n/2; i++){
        // Pick Current Letter and Store in Temp
        char temp = s[i];
        // Get Letter From Last and then Swap them both
        s[i] = s[n-1-i];
        s[n-1-i] = temp;
    }

    cout << "Reversed String: " << s << "\n";
}   