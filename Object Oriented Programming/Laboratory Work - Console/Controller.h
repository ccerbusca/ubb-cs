//
// Created by Cristian Cerbusca on 2019-03-24.
//

#ifndef LAB5_6_CONTROLLER_H
#define LAB5_6_CONTROLLER_H


#include "Repository.h"
#include "FileRepository.h"
#include <stdexcept>

class Controller {
private:
	Repository* _repository;
	Repository* _watchList;
public:
	explicit Controller(Repository* repository, Repository *watchList);
	void add(const std::string& Title, const std::string& Genre, const std::string& Trailer,
	         int YearOfRelease, int NumberOfLikes);
	void save(Movie movie);
	void update(const std::string& Title, const std::string& Genre, const std::string& Trailer,
	            int YearOfRelease, int NumberOfLikes);
	void remove(const std::string& title);
	const int size() const { return _repository->size(); }
	const std::vector<Movie> & getMovies() const { return _repository->getData(); }
	const std::vector<Movie> & getWatchList() const { return _watchList->getData(); }
	void display();
	~Controller();
};


#endif //LAB5_6_CONTROLLER_H
