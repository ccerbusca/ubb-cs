//
// Created by Cristian Cerbusca on 2019-03-24.
//


#include "Controller.h"
#include "utils.h"
#include "Validator.h"

Controller::Controller(Repository *otherRepository, Repository *watchList):
					_repository{otherRepository}, _watchList{watchList} {}

/**
 * The function adds a new Movie entry to the database with the specified fields
 * @param Title - title of the movie
 * @param Genre - genre of the movie
 * @param Trailer - a link to a online resource with a trailer to the movie
 * @param YearOfRelease - the movie's year of release
 * @param NumberOfLikes - the movie's number of likes
 */
void Controller::add(const std::string &Title, const std::string &Genre, const std::string &Trailer,
						int YearOfRelease, int NumberOfLikes) {

	if (_repository->exists(Title))
		throw std::runtime_error("A movie with the same title already exists.");
	Movie movie{Title, Genre, Trailer, YearOfRelease, NumberOfLikes};
	if (Validator::validateMovie(movie))
		this->_repository->add(movie);
}

void Controller::save(Movie movie) {
	if (_watchList->exists(movie.title))
		throw std::runtime_error("The movie is already in your watch-list.");
	this->_watchList->add(movie);
}

/**
 * The function updates the fields of the Movie identified by the specified title
 * @param Title - title of the movie to be updated
 * @param newGenre
 * @param newTrailer
 * @param newYearOfRelease
 * @param newNumberOfLikes
 */
void Controller::update(const std::string &Title, const std::string &newGenre, const std::string &newTrailer,
                        int newYearOfRelease, int newNumberOfLikes) {
	_repository->update(Title, newGenre, newTrailer, newYearOfRelease, newNumberOfLikes);
}

/**
 * Removes the movie with the specified title
 * @param title
 */
void Controller::remove(const std::string &title) {
	_repository->remove(title);
}

void Controller::display()
{
	_watchList->display();
}

Controller::~Controller() {
	delete _watchList;
	delete _repository;
}
