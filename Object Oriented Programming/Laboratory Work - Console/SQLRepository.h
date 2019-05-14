#pragma once
#include "Repository.h"
#include "FileRepository.h"

class SQLRepository :
	public Repository
{
private:
	std::string databaseName;
	const std::vector<Movie> selectAll(std::string query) const;
public:
	SQLRepository(std::string dbName);
	void add(const Movie& element) override;
	void update(const std::string &Title, const std::string &newGenre, const std::string &newTrailer, int newYearOfRelease, int newNumberOfLikes) override;
	void remove(const std::string &Title) override;
	bool exists(const std::string &Title) override;
	int size() const override;
	const std::vector<Movie>& getData() override;
	void display() override {}
};

