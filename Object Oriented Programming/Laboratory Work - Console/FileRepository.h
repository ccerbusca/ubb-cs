//
// Created by Cristian Cerbusca on 2019-04-14.
//

#ifndef LAB5_6_FILEREPOSITORY_H
#define LAB5_6_FILEREPOSITORY_H


#include <istream>
#include "Repository.h"
#include "FileRepositoryBase.h"

class FileRepository: public FileRepositoryBase {
public:
	FileRepository(std::string name);
	void readFromFile() override;
	void writeToFile() override;
	void display() override;
	void add(const Movie& element) override;
	void update(const std::string &Title, const std::string &newGenre,
			const std::string &newTrailer, int newYearOfRelease,
			int newNumberOfLikes) override;
	void remove(const std::string &Title) override;
	bool exists(const std::string &Title) override;
	int size() const override;
	const std::vector<Movie>& getData() override;
};


#endif //LAB5_6_FILEREPOSITORY_H
