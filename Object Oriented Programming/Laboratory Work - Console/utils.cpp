//
// Created by Cristian Cerbusca on 2019-04-14.
//

#include <sstream>
#include <algorithm>
#include "utils.h"


/**
 * The following function receives a string as input and split it into words, using space and comma as separators
 * @param inputString
 * @return vector of words
 */
std::vector<std::string> utils::splitInput(const std::string &inputString) {
	std::vector<std::string> wordVector;
	std::stringstream stringStream(inputString);
	std::string line;
	while(std::getline(stringStream, line))
	{
		std::size_t previousPosition = 0, positionFound;
		while ((positionFound = line.find_first_of(" ,", previousPosition)) != std::string::npos)
		{
			if (positionFound > previousPosition)
				wordVector.push_back(line.substr(previousPosition, positionFound-previousPosition));
			previousPosition = positionFound+1;
		}
		if (previousPosition < line.length())
			wordVector.push_back(line.substr(previousPosition, std::string::npos));
	}
	return wordVector;
}

/**
 * Checks whether a string is made up of only digits
 * @param string
 * @return true/false
 */
bool utils::is_number(const std::string &string) {
	return !string.empty() && std::find_if(string.begin(),
	                                  string.end(), [](char c) { return !isdigit(c); }) == string.end();
}