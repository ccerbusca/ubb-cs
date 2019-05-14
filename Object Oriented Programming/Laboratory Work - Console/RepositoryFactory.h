#pragma once
#include "Repository.h"
#include "FileRepository.h"
#include "HTMLRepository.h"
//#include "SQLRepository.h"

class RepositoryFactory
{
public:
	static Repository* createRepository(std::string filePath);
};
