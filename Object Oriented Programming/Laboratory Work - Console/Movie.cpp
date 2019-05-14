//
// Created by Cristian Cerbusca on 2019-03-24.
//

#include "Movie.h"
#include "utils.h"

Movie::Movie(): title{""}, genre{""}, trailer{""}, yearOfRelease{0}, numberOfLikes{0}
{
}

Movie::Movie(const std::string& Title, const std::string& Genre, const std::string& Trailer,
		int YearOfRelease, int NumberOfLikes): title{Title}, genre{Genre},
		trailer{Trailer}, yearOfRelease{YearOfRelease}, numberOfLikes{NumberOfLikes}
{
}

/**
 * The following function returns a formatted string to represent the movie entity
 * @return - string
 */
std::string Movie::toString() const {
	return this->title +
           "; Genre: " + this->genre +
           "; Year of Release: " + std::to_string(this->yearOfRelease) +
           "; Number of likes: " + std::to_string(this->numberOfLikes) +
           "; Link to the trailer: " + this->trailer;
}

 bool Movie::operator==(const Movie & movie)
 {
	 return this->title == movie.title &&
		 this->genre == movie.genre &&
		 this->trailer == movie.trailer &&
		 this->numberOfLikes == movie.numberOfLikes &&
		 this->yearOfRelease == movie.yearOfRelease;
 }

/**
 * Copy constructor of the Movie entity
 * @param movie
 */
Movie::Movie(const Movie &movie) {
	title = movie.title;
	genre = movie.genre;
	trailer = movie.trailer;
	numberOfLikes = movie.numberOfLikes;
	yearOfRelease = movie.yearOfRelease;
}

/**
 * The extraction operator overloading for the Movie entity
 * @param is - input stream
 * @param movie - movie object
 * @return - the input stream's state after the insertion
 */
std::istream& operator>>(std::istream& is, Movie& movie) {
	std::string line;
	getline(is, line);
	auto tokens = utils::splitInput(line);
	if (tokens.size() != 5)
		return is;
	movie.title = tokens[0];
	movie.genre = tokens[1];
	movie.yearOfRelease = std::stoi(tokens[2]);
	movie.numberOfLikes = std::stoi(tokens[3]);
	movie.trailer = tokens[4];
	return is;
}

/**
 * The insertion operator overloading for the Movie entity
 * @param os - output stream
 * @param movie - movie object
 * @return - the output stream's state after the insertion
 */
std::ostream& operator<<(std::ostream& os, const Movie& movie) {
	os << movie.title << std::string(",") << movie.genre << std::string(",") << std::to_string(movie.yearOfRelease) <<
			std::string(",") << std::to_string(movie.numberOfLikes) << std::string(",") << movie.trailer << std::string("\n");
	return os;
}