//
// Created by Cristian Cerbusca on 2019-03-24.
//

#ifndef LAB5_6_UI_H
#define LAB5_6_UI_H


#include "Controller.h"
#include <iostream>
#include <iterator>
#include <vector>
#include <stdexcept>
#include <functional>
#include "utils.h"
#include "Validator.h"

class UI {
private:
	Controller& controller;
	int mode;
	std::size_t currentPosition;
public:
	explicit UI(Controller& controller);
	void start();
	void adminMenu();
	void userMenu();
	static void list_filteredList(const std::vector<Movie>& repository, std::function<bool(Movie&)> filterFunction);
	~UI();

};


#endif //LAB5_6_UI_H
