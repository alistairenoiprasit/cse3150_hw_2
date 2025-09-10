//
// Created by Alistaire Noiprasit on 10/9/2025.
//
#include "../include/greeting_utils.h"
#include <iostream>
#include <string>

using std::cout, std::cin, std::endl;

std::string GreetingUtils::create_message(const std::string& name) {
        return ("Hello, " + name + "!");
}

char* GreetingUtils::format_as_c_string(const std::string& msg) {
        char* c_str = new char[msg.length() + 1];
        for (unsigned int i = 0; i < msg.length(); i++) {
                c_str[i] = msg[i];
        }
        c_str[msg.length()] = '\0';
        return c_str;
}