#include "SQLRepository.h"
#include <iostream>
#include <winsqlite/winsqlite3.h>


SQLRepository::SQLRepository(std::string name):databaseName{name}
{
	sqlite3* database;
	int exit = 0;
	exit = sqlite3_open(databaseName.c_str(), &database);

	if (exit != SQLITE_OK) {
		throw std::runtime_error("ERROR Opening database");
	}

	std::string query = "CREATE TABLE IF NOT EXISTS MOVIES("
						"title TEXT PRIMARY KEY NOT NULL,"
						"genre TEXT NOT NULL,"
						"trailer TEXT NOT NULL,"
						"year INTEGER NOT NULL,"
						"like INTEGER NOT NULL);";
	char *messageError;
	exit = sqlite3_exec(database, query.c_str(), NULL, 0, &messageError);

	if (exit != SQLITE_OK) {
		std::string exceptionError = std::string("Error when creating Table: ") + std::string(messageError);
		sqlite3_free(messageError);
		throw std::runtime_error(exceptionError);
	}
	sqlite3_close(database);
}

void SQLRepository::add(const Movie & element){
	sqlite3* database;
	char* messageError;
	int exit = sqlite3_open(databaseName.c_str(), &database);

	std::string sql = "INSERT INTO MOVIES VALUES(" +
				std::string("'") + element.title + std::string("'") + ", " +
				std::string("'") + element.genre + std::string("'") + ", " +
				std::string("'") + element.trailer + std::string("'") + ", " +
				std::to_string(element.yearOfRelease) + ", " +
				std::to_string(element.numberOfLikes) + ");";

	exit = sqlite3_exec(database, sql.c_str(), NULL, 0, &messageError);
	if (exit != SQLITE_OK) {
		std::string exceptionError = std::string("Error when inserting into the table: ") + std::string(messageError);
		sqlite3_free(messageError);
		throw std::runtime_error(exceptionError);
	}
	sqlite3_close(database);
}

void SQLRepository::update(const std::string & Title, const std::string & newGenre,
			const std::string & newTrailer, int newYearOfRelease, int newNumberOfLikes){
	sqlite3* database;
	char* messageError;
	int exit = sqlite3_open(databaseName.c_str(), &database);

	std::string sql = "UPDATE MOVIES "
		"SET "
		"genre = '" + newGenre + "',"
		"trailer = '" + newTrailer + "',"
		"year = '" + std::to_string(newYearOfRelease) + "',"
		"like = '" + std::to_string(newNumberOfLikes) + "' "
		"WHERE title = '" + Title + "';";
					
	exit = sqlite3_exec(database, sql.c_str(), NULL, 0, &messageError);
	if (exit != SQLITE_OK) {
		std::string exceptionError = std::string("Error when updating the table: ") + std::string(messageError);
		sqlite3_free(messageError);
		throw std::runtime_error(exceptionError);
	}
	sqlite3_close(database);
}

void SQLRepository::remove(const std::string & Title) {
	sqlite3* database;
	char* messageError;
	int exit = sqlite3_open(databaseName.c_str(), &database);

	std::string sql = "DELETE FROM MOVIES WHERE title = '" + Title + "';";
	exit = sqlite3_exec(database, sql.c_str(), NULL, 0, &messageError);
	if (exit != SQLITE_OK) {
		std::string exceptionMessage = std::string("Error when deleting from table: ") + std::string(messageError);
		sqlite3_free(messageError);
		throw std::runtime_error(exceptionMessage);
	}
	sqlite3_close(database);
}

bool SQLRepository::exists(const std::string & Title)
{
	return selectAll("WHERE title = '" + Title + "';").size() > 0;
}

int SQLRepository::size() const
{
	return selectAll(";").size();
}

static int _stdcall callback(void* data, int argumentCount, char** arguments, char** columnNames)
{
	std::vector<Movie> *vector = static_cast<std::vector<Movie>*>(data);
	vector->push_back(Movie{ arguments[0], arguments[1], arguments[2], std::stoi(arguments[3]), std::stoi(arguments[4]) });
	return 0;
}

const std::vector<Movie>& SQLRepository::getData()
{
	vector = selectAll(";");
	return vector;
}

const std::vector<Movie> SQLRepository::selectAll(std::string query) const
{
	sqlite3* database;
	int exit = 0;
	std::vector<Movie> movies;
	exit = sqlite3_open(databaseName.c_str(), &database);
	char* messageError;

	std::string sql("SELECT * FROM MOVIES " + query);
	if (exit != SQLITE_OK) {
		throw std::runtime_error("Error open DB " + std::string(sqlite3_errmsg(database)));
	}
	exit = sqlite3_exec(database, sql.c_str(), callback, (void*)(&movies), &messageError);

	if (exit != SQLITE_OK) {
		std::string exceptionMessage = std::string("Error when deleting from table: ") + std::string(messageError);
		sqlite3_free(messageError);
		throw std::runtime_error(exceptionMessage);
	}

	sqlite3_close(database);
	return movies;
}
