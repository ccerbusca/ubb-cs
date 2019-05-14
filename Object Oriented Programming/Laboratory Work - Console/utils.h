//
// Created by Cristian Cerbusca on 2019-04-14.
//

#ifndef LAB8_UTILS_H
#define LAB8_UTILS_H

#include <vector>
#include <string>

class utils {
public:
	static std::vector<std::string> splitInput(const std::string &inputString);
	static bool is_number(const std::string& string);
};


#endif //LAB8_UTILS_H
