//
// Created by Cristian Cerbusca on 2019-03-24.
//

#ifndef LAB5_6_REPOSITORY_H
#define LAB5_6_REPOSITORY_H


#include <vector>
#include <algorithm>
#include "Movie.h"

class Repository {
protected:
	std::vector<Movie> vector;
public:
	virtual void add(const Movie& element);
	virtual void update(const std::string &Title, const std::string &newGenre, const std::string &newTrailer, int newYearOfRelease, int newNumberOfLikes);
	virtual void remove(const std::string &Title);
	virtual bool exists(const std::string &Title);
	virtual int size() const;
	virtual const std::vector<Movie>& getData();
	virtual void display();
};


#endif //LAB5_6_REPOSITORY_H
