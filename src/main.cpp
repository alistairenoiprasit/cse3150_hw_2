//
// Created by Alistaire Noiprasit on 10/9/2025.
//
#include "../include/greeting_utils.h"
#include <iostream>
#include <string>

int main() {
    using namespace std;
    cout << "Enter your name please: " << endl;
    string full_name;

    getline(cin, full_name);

    using namespace GreetingUtils;
    char* greeting_c = format_as_c_string(create_message(full_name));
    cout << greeting_c << endl;
    delete[] greeting_c;
}