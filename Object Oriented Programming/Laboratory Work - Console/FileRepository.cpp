#include <utility>

//
// Created by Cristian Cerbusca on 2019-04-14.
//

#include "FileRepository.h"
#include <fstream>
#include "Movie.h"

FileRepository::FileRepository(std::string name)
{
	fileName = name;
}

/**
 * The following function populates the repository with values from the file, with the name
 * in fileName
 */

void FileRepository::readFromFile() {
	vector.clear();
	std::ifstream inputStream(fileName);
	Movie movie;
	while (inputStream >> movie) {
		Repository::add(movie);
	}
	inputStream.close();
}


/**
 * Writes the repository data to the repository file
 */
void FileRepository::writeToFile() {
	std::ofstream outputStream(fileName);
	for (const auto& i : vector) {
		outputStream << i;
	}
	outputStream.close();
}

void FileRepository::display() {
	std::string command = "notepad \"" + fileName + "\"";
	system(command.c_str());
}

void FileRepository::add(const Movie& element) {
	this->readFromFile();
	Repository::add(element);
	this->writeToFile();
}

void FileRepository::update(const std::string & Title, const std::string & newGenre, const std::string & newTrailer, int newYearOfRelease, int newNumberOfLikes)
{
	this->readFromFile();
	Repository::update(Title, newGenre, newTrailer, newYearOfRelease, newNumberOfLikes);
	this->writeToFile();
}

void FileRepository::remove(const std::string & Title){
	this->readFromFile();
	Repository::remove(Title);
	this->writeToFile();
}

bool FileRepository::exists(const std::string & Title)
{
	this->readFromFile();
	return Repository::exists(Title);
}

int FileRepository::size() const
{
	return Repository::size();
}

const std::vector<Movie>& FileRepository::getData()
{
	this->readFromFile();
	return vector;
}
