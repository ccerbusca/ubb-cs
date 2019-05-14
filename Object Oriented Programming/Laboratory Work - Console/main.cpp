#include <iostream>
#include "Movie.h"
#include "Repository.h"
#include "Controller.h"
#include "UI.h"
#include "Tests.h"
//#include "SQLRepository.h"
#include "HTMLRepository.h"
#include "RepositoryFactory.h"

int main() {
	//test_All();

	bool repoLocationEntered = false;
	std::string path = "";
	while (!repoLocationEntered) {
		try {
			char inputString[300];
			std::cin.getline(inputString, 300);
			if (strlen(inputString) == 0)
				throw std::runtime_error("Invalid command");
			auto input = utils::splitInput(inputString);
			std::size_t position;
			std::string cToString = inputString;
			position = cToString.find_first_of(' ', 0);
			path = cToString.substr(position + 1);
			if (input.size() <= 0)
				throw std::runtime_error("Invalid command");
			if (input[0] == "fileLocation") {
				if (position != std::string::npos) {
					repoLocationEntered = true;
				}
				else
					throw std::runtime_error("Wrong number of arguments");
			}
			else if (input[0] == "exit")
				return 0;
			else
				throw std::runtime_error("Enter the repository file location, please");
		}
		catch (std::runtime_error& error) {
			std::cout << error.what() << std::endl;
		}
	}

	bool watchListLocationEntered = false;
	std::string watchListPath;
	while (!watchListLocationEntered) {
		try {
			char inputString[100];
			std::cin.getline(inputString, 100);
			if (strlen(inputString) == 0)
				throw std::runtime_error("Invalid command");
			auto input = utils::splitInput(inputString);
			std::size_t position;
			std::string cToString = inputString;
			position = cToString.find_first_of(' ', 0);
			watchListPath = cToString.substr(position + 1);
			if (input.size() <= 0)
				throw std::runtime_error("Invalid command");
			if (input[0] == "mylistLocation") {
				if (position != std::string::npos) {
					watchListLocationEntered = true;
				}
				else
					throw std::runtime_error("Wrong number of arguments");
			}
			else if (input[0] == "exit")
				return 0;
			else
				throw std::runtime_error("Enter the watch list file location, please");
		}
		catch (std::runtime_error& error) {
			std::cout << error.what() << std::endl;
		}
	}


	Controller controller{ RepositoryFactory::createRepository(path),
							RepositoryFactory::createRepository(watchListPath) };
	UI ui{controller};
	ui.start();
	return 0;
}