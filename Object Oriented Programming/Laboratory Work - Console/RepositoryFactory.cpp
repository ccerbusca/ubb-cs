#include "RepositoryFactory.h"
#include <iostream>
Repository * RepositoryFactory::createRepository(std::string filePath) {
	std::size_t position = filePath.find_last_of('.');
	std::string extension = "";
	if (position != std::string::npos)
		 extension = filePath.substr(position);
	if (extension == ".csv" or extension == ".txt") {
		return new FileRepository{ filePath };
	}
	/*else if (extension == ".db") {
		
		return new SQLRepository{ filePath };
	}*/
	else if (extension == ".html") {
		return new HTMLRepository{ filePath };
	}
	else {
		return new Repository;
	}
}
