//
// Created by Cristian Cerbusca on 2019-03-24.
//

#include <algorithm>
#include "UI.h"
#include <cstring>
#include <utility>

UI::UI(Controller &controller): controller{controller}, currentPosition{0}, mode{0} {}

UI::~UI() {}

void UI::start() {
	mode = 0;
	while(true)
	{
		try {
			if (mode != 1 && mode != 2 && mode != 3) {
				char inputString[300];
				std::cin.getline(inputString, 300);
				auto wordVector = utils::splitInput(inputString);
				if (wordVector.size() == 2)
				{
					if (wordVector[0] == "mode") {
						if (wordVector[1] == "A")
							mode = 1;
						else if (wordVector[1] == "B")
							mode = 2;
						else
							std::cout << "Invalid mode" << std::endl;
					}
					else
						std::cout << "Please, specify the mode" << std::endl;
				}
				else if (wordVector.size() == 1 and wordVector[0] == "exit")
					mode = 3;
				else
					std::cout<<"Please, specify the mode" << std::endl;
			} else if (mode == 1) {
				adminMenu();
			} else if (mode == 2) {
				userMenu();
			}
			else if (mode == 3)
				return;
		} catch (std::runtime_error& error) {
			std::cout<< error.what() << std::endl;
		}
	}
}

void UI::list_filteredList(const std::vector<Movie>& elements, std::function<bool(Movie&)> filterFunction) {
	std::vector<Movie> filteredElements;
	for (const Movie& i : elements) {
		Movie someMovie = i;
		if (filterFunction(someMovie)) {
			filteredElements.push_back(someMovie);
		}
	}
	for (auto& i : filteredElements)
		std::cout<< i.toString() << std::endl;
}

void UI::userMenu() {
	char inputLine[256];
	while(true) {
		try {
			std::cin.getline(inputLine, 256);
			if (strlen(inputLine) == 0)
				throw std::runtime_error("Invalid command");
			std::vector<std::string> input = utils::splitInput(inputLine);
			if (input.size() <= 0)
				throw std::runtime_error("Invalid command");
			if (input[0] == "list") {
				if (input.size() == 3) {
					list_filteredList(controller.getMovies(),
							    [&input](Movie &movie) {
					                  return movie.genre == input[1] && 
					                         movie.numberOfLikes >= std::stoi(input[2]);
				                  });
				}
				else if (input.size() == 2) {
					list_filteredList(controller.getMovies(),
								[&input](Movie &movie) {
									  return movie.genre == input[1];
								  });
				}
				else if (input.size() == 1) {
					list_filteredList(controller.getMovies(), [](Movie& movie) { return true; });
				} else
					throw std::runtime_error("Wrong number of parameters");
			} else if (input[0] == "mylist") {
				controller.display();
			} else if (input [0] == "next") {
				if (controller.getMovies().size() > 0) {
					if (currentPosition >= controller.getWatchList().size())
						currentPosition = 0;
					std::cout << controller.getMovies().at(currentPosition).toString() << std::endl;
					currentPosition++;
				}
			} else if (input [0] == "save") {
				if (input.size() == 2) {
					auto moviesList = controller.getMovies();
					auto movie = std::find_if(moviesList.begin(), moviesList.end(),
							[&input](Movie& movie) { return movie.title == input[1]; });
					if (movie != moviesList.end())
						controller.save(*movie);
					else
						throw std::runtime_error("No such movie");
				} else
					throw std::runtime_error("Wrong number of arguments");
			} else if (input[0] == "exit") {
				mode = 3;
				return;
			} else if (input[0] == "mode") {
				if (input.size() == 2) {
					if (input[1] == "A")
						mode = 1;
					else if (input[1] == "B")
						mode = 2;
					break ;
				} else
					throw std::runtime_error("Wrong number of parameters");
			} else
				std::cout << "Invalid command" << std::endl;
		}
		catch (std::runtime_error &error) {
			std::cout << error.what() << std::endl;
		}
	}
}

void UI::adminMenu() {
	char inputLine[256];
	while(true) {
		try {
			std::cin.getline(inputLine, 256);
			if (strlen(inputLine) == 0)
				throw std::runtime_error("Invalid command");
			std::vector<std::string> input = utils::splitInput(inputLine);
			if (input.size() <= 0)
				throw std::runtime_error("Invalid command");
			if (input[0] == "add") {
				if (input.size() == 6) {
					if (!utils::is_number(input[3]))
						throw std::runtime_error("Year of release is not an integer.");
					if (!utils::is_number(input[4]))
						throw std::runtime_error("Number of likes is not an integer.");
					controller.add(input[1], input[2], input[5], std::stoi(input[3]),
					               std::stoi(input[4]));
				}
				else
					throw std::runtime_error("Wrong number of parameters");
			} else if (input[0] == "update") {
				if (input.size() == 6)
					controller.update(input[1], input[2], input[5], std::stoi(input[3]),
				                  std::stoi(input[4]));
				else
					throw std::runtime_error("Wrong number of parameters");
			} else if (input[0] == "delete") {
				if (input.size() == 2)
					controller.remove(input[1]);
				else
					throw std::runtime_error("Wrong number of parameters");
			} else if (input[0] == "list" && mode == 1) {
				if (input.size() == 1)
					list_filteredList(controller.getMovies(), [](Movie& movie) { return true; });
				else
					throw std::runtime_error("Wrong number of parameters");
			} else if (input[0] == "exit") {
				mode = 3;
				return;
			} else if (input[0] == "mode") {
				if (input.size() == 2)
				{
					if (input[1] == "A")
						mode = 1;
					else if (input[1] == "B") {
						mode = 2;
						currentPosition = 0;
					}
					break;
				}
				else
					throw std::runtime_error("Wrong number of parameters");
			}
			else
				std::cout << "Invalid command" << std::endl;
		}
		catch (std::runtime_error& error){
			std::cout << error.what() << std::endl;
		}
	}
}

