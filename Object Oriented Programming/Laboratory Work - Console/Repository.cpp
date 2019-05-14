#include "Repository.h"
#include <iostream>

void Repository::add(const Movie& element) {
	/**
	 * The function adds and element to the Dynamic Vector
	 */
	vector.push_back(element);
}
void Repository::update(const std::string &Title, const std::string &newGenre, const std::string &newTrailer,
	int newYearOfRelease, int newNumberOfLikes) {
	/**
	 * The function finds a Movie with the specified title and updates it's properties
	 */
	for (auto& movie : vector)
		if (movie.title == Title)
		{
			movie.genre = newGenre;
			movie.trailer = newTrailer;
			movie.yearOfRelease = newYearOfRelease;
			movie.numberOfLikes = newNumberOfLikes;
			break;
		}
}
void Repository::remove(const std::string &Title) {
	/**
	 * The function removes the Movie with the specified title
	 */
	auto found = std::find_if(vector.begin(), vector.end(), [&Title](Movie& a) { return a.title == Title; });
	if (found != vector.end())
		vector.erase(found);
}

bool Repository::exists(const std::string &Title) {
	/**
	 * The function checks if a movie with the given title exists in the repository
	 */
	auto elementFound = std::find_if(vector.begin(), vector.end(), [&Title](Movie& a) { return a.title == Title; });
	return elementFound != vector.end();
}

/**
 * Getter for the size of the Dynamic Vector
 * @return size of the Dynamic Vector
 */
int Repository::size() const { return vector.size(); }
const std::vector<Movie>& Repository::getData(){
	return this->vector;
}

void Repository::display()
{
	for (const auto &i : vector) {
		std::cout << i.toString() << std::endl;
	}
}
