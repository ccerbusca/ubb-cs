#pragma once
#include "FileRepository.h"
#include <Windows.h>
#include <shellapi.h>

class HTMLRepository :
	public FileRepositoryBase
{
protected:
	std::string fileName;
public:
	HTMLRepository(std::string name);
	void writeToFile() override;
	void readFromFile() override {}
	void display() override;
};

