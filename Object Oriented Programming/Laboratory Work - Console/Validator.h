#pragma once

#include <string>
#include <cctype>
#include <algorithm>
#include "Movie.h"

class Validator
{
public:
	static bool validateMovie(const Movie& movie);
};

class ValidationError : public std::exception {
private:
	std::string message;
public:
	ValidationError(std::string& message): message{message} {}
	ValidationError(const char* message) : message{ message } {}
	virtual char const * what() const { return message.c_str(); }
};

