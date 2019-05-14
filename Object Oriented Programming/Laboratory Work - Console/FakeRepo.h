#pragma once
#include "Repository.h"
class FakeRepo :
	public Repository
{
public:
	bool exists(const std::string &Title) override;
};

