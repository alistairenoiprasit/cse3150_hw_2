//
// Created by Alistaire Noiprasit on 10/9/2025.
//

#ifndef GREETING_UTILS_H
#define GREETING_UTILS_H
#include <string>
#endif //GREETING_UTILS_H

namespace GreetingUtils {
    std::string create_message(const std::string& name);
    char* format_as_c_string(const std::string& msg);
}
