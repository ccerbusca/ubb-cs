#pragma once
#include "Repository.h"
class FileRepositoryBase :
	public Repository
{
protected:
	std::string fileName;
public:
	virtual void writeToFile() = 0;
	virtual void readFromFile() = 0;
};


