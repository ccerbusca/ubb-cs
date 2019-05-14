#include "FakeRepo.h"


bool FakeRepo::exists(const std::string & Title)
{
	if (Title == "1")
		return true;
	else
		return false;
}