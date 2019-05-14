//
// Created by Cristian Cerbusca on 2019-03-24.
//

#ifndef LAB5_6_MOVIE_H
#define LAB5_6_MOVIE_H


#include <string>
#include <fstream>

class Movie {
public:
	std::string title, genre, trailer;
	int numberOfLikes, yearOfRelease;

	Movie();
	Movie(const Movie& movie);
	Movie(const std::string& Title, const std::string& Genre, const std::string& Trailer,
			int YearOfRelease, int NumberOfLikes);
	std::string toString() const;
	bool operator==(const Movie & movie);
};

std::istream& operator>>(std::istream& is, Movie& movie);
std::ostream& operator<<(std::ostream& os, const Movie& movie);

#endif //LAB5_6_MOVIE_H
