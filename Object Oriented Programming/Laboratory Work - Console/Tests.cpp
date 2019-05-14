//
// Created by Cristian Cerbusca on 2019-03-25.
//

#include "Repository.h"
#include "HTMLRepository.h"
//#include "SQLRepository.h"
#include "Controller.h"
#include <assert.h>
#include "utils.h"
#include "RepositoryFactory.h"
#include "FakeRepo.h"
#include "Validator.h"

void test_NONTRIVIALFUNCTION() {
	FakeRepo repository;
	repository.add(Movie{ "1", "2", "3", 4, 5 });
	assert(repository.exists("1"));
	assert(!repository.exists("2"));
}

void add_valid() {
	Repository *repository = new Repository;
	Repository *watchList = new Repository;
	Controller controller{ repository, watchList };
	std::string title = "1";
	std::string genre = "2";
	std::string trailer = "3";
	controller.add(title, genre, trailer, 4, 5);
	assert(controller.getMovies().size() == 1);
}

void add_invalid() {
	Repository *repository = new Repository;
	Repository *watchList = new Repository;
	Controller controller{ repository, watchList };
	controller.add("1", "2", "3", 4, 5);
	try {
		controller.add("1", "2", "3", 4, 5);
		assert(false);
	}
	catch (std::runtime_error& error) {
		assert(true);
	}
}

void save_valid() {
	Repository *repository = new Repository;
	Repository *watchList = new Repository;
	Controller controller{ repository, watchList };
	controller.save(Movie{ "title", "genre", "trailer", 4, 5 });
	assert(controller.getWatchList().size() == 1);
}

void save_invalid() {
	Repository *repository = new Repository;
	Repository *watchList = new Repository;
	Controller controller{ repository, watchList };
	controller.save(Movie{ "1", "2", "3", 4, 5 });
	try {
		controller.save(Movie{ "1", "2", "3", 4, 5 });
		assert(false);
	}
	catch (std::runtime_error& error) {
		assert(true);
	}
}

void updateController() {
	Repository *repository = new Repository;
	Repository *watchList = new Repository;
	Controller controller{ repository, watchList };
	controller.add("1", "2", "3", 4, 5);
	controller.update("1", "3", "4", 5, 6);
	auto movie = controller.getMovies().at(0);
	assert(movie.title == "1");
	assert(movie.genre == "3");
	assert(movie.trailer == "4");
	assert(movie.yearOfRelease == 5);
	assert(movie.numberOfLikes == 6);
}

void removeController() {
	Repository *repository = new Repository;
	Repository *watchList = new Repository;
	Controller controller{ repository, watchList };
	controller.add("1", "2", "3", 4, 5);
	controller.remove("1");
	assert(repository->size() == 0);
}

void movie_test() {
	Movie movie{ "1", "2", "3", 4, 5 };
	assert(movie.title == "1");
	assert(movie.genre == "2");
	assert(movie.trailer == "3");
	assert(movie.yearOfRelease == 4);
	assert(movie.numberOfLikes == 5);
}

void movie_toString() {
	Movie movie{ "1", "2", "3", 4, 5 };
	auto string = movie.title +
		"; Genre: " + movie.genre +
		"; Year of Release: " + std::to_string(movie.yearOfRelease) +
		"; Number of likes: " + std::to_string(movie.numberOfLikes) +
		"; Link to the trailer: " + movie.trailer;
	assert(movie.toString() == string);
}

void file_write_test() {
	{
		std::remove("D:\\testfile");
		std::remove("D:\\wtestfile");
		FileRepository *repository = new FileRepository{"D:\\testfile"};
		FileRepository *watchList = new FileRepository{ "D:\\wtestfile" };
		Controller controller{ repository, watchList };
		controller.add("1", "2", "3", 4, 5);
	}
	{
		FileRepository *repository = new FileRepository{ "D:\\testfile" };
		FileRepository *watchList = new FileRepository{ "D:\\wtestfile" };
		Controller controller{ repository, watchList };
		auto movie = controller.getMovies().at(0);
		assert(movie.title == "1");
		assert(movie.genre == "2");
		assert(movie.trailer == "3");
		assert(movie.yearOfRelease == 4);
		assert(movie.numberOfLikes == 5);
	}
	std::remove("D:\\testfile");
	std::remove("D:\\wtestfile");
}

void utils_isNumber() {
	assert(utils::is_number("1234"));
	assert(!utils::is_number("abcd"));
	assert(!utils::is_number("1abc"));
}

void test_HTML_file() {
	{
		HTMLRepository watchList{ "D:\\test.html" };
		watchList.add(Movie{ "1", "2", "3", 4, 5 });
		watchList.writeToFile();
		std::ifstream inputStream("D:\\test.html");
		char inputLine[300];
		for (int i = 0; i < 12; i++)
			inputStream.getline(inputLine, 300);
		inputStream.getline(inputLine, 300);
		std::string line(inputLine);
		size_t pos = line.find("<td>");
		assert(pos != std::string::npos);
		line.erase(pos, 4); 
		pos = line.find("</td>");
		assert(pos != std::string::npos);
		line.erase(pos, 5);
		assert(line == "1");

		inputStream.getline(inputLine, 300);
		line =inputLine;
		pos = line.find("<td>");
		assert(pos != std::string::npos);
		line.erase(pos, 4);
		pos = line.find("</td>");
		assert(pos != std::string::npos);
		line.erase(pos, 5);
		assert(line == "2");

		inputStream.getline(inputLine, 300);
		line = inputLine;
		pos = line.find("<td>");
		assert(pos != std::string::npos);
		line.erase(pos, 4);
		pos = line.find("</td>");
		assert(pos != std::string::npos);
		line.erase(pos, 5);
		assert(line == "4");

		inputStream.getline(inputLine, 300);
		line = inputLine;
		pos = line.find("<td>");
		assert(pos != std::string::npos);
		line.erase(pos, 4);
		pos = line.find("</td>");
		assert(pos != std::string::npos);
		line.erase(pos, 5);
		assert(line == "5");

		inputStream.getline(inputLine, 300);
		line = inputLine;
		pos = line.find("<td>");
		assert(pos != std::string::npos);
		line.erase(pos, 4);
		pos = line.find("</td>");
		assert(pos != std::string::npos);
		line.erase(pos, 5);
		assert(line == "3");
	}
	std::remove("D:\\test.html");
}

void test_FileRepo_size() {
	{
		FileRepository repository{ "D:\\test.csv" };
		assert(repository.size() == 0);
		repository.add(Movie{ "1", "2", "3", 4, 5 });
		assert(repository.size() == 1);
		repository.remove("1");
		assert(repository.size() == 0);
	}
	std::remove("D:\\test.csv");
}

void test_FileRepo_remove() {
	{
		FileRepository repository{ "D:\\test.csv" };
		repository.add(Movie{ "1", "2", "3", 4, 5 });
		assert(repository.exists("1"));
		repository.remove("1");
		assert(!repository.exists("1"));
	}
	std::remove("D:\\test.csv");
}

void test_FileRepo_update() {
	{
		FileRepository repository{ "D:\\test.csv" };
		repository.add(Movie{ "1", "2", "3", 4, 5 });
		repository.update("1", "200", "300", 400, 500);
		Movie movie = repository.getData().at(0);
		Movie movie2 = Movie{ "1", "200", "300", 400, 500 };
		assert(movie == movie2);
	}
	std::remove("D:\\test.csv");
}

void test_RepositoryFactory() {
	{
		std::string csv_path("D:\\test.csv");
		std::string sql_path("D:\\test.db");
		std::string txt_path("D:\\test.txt");
		std::string html_path("D:\\test.html");
		std::string simple_path("");
		assert(typeid(*RepositoryFactory::createRepository(csv_path)) == typeid(FileRepository));
		/*assert(typeid(*RepositoryFactory::createRepository(sql_path)) == typeid(SQLRepository));*/
		assert(typeid(*RepositoryFactory::createRepository(txt_path)) == typeid(FileRepository));
		assert(typeid(*RepositoryFactory::createRepository(html_path)) == typeid(HTMLRepository));
		assert(typeid(*RepositoryFactory::createRepository(simple_path)) == typeid(Repository));
	}
}

//void test_SQL_add() {
//	{
//		SQLRepository repository{ "D:\\myTest.db" };
//		repository.add(Movie{ "1", "2", "3", 4, 5 });
//		assert(repository.exists("1"));
//		assert(repository.size() == 1);
//		auto movie = repository.getData().at(0);
//		assert(movie.title == "1");
//		assert(movie.genre == "2");
//		assert(movie.trailer == "3");
//		assert(movie.yearOfRelease == 4);
//		assert(movie.numberOfLikes == 5);
//	}
//	std::remove("D:\\myTest.db");
//}
//
//void test_SQL_remove() {
//	{
//		SQLRepository repository{ "D:\\myTest.db" };
//		repository.add(Movie{ "1", "2", "3", 4, 5 });
//		assert(repository.size() == 1);
//		repository.remove("1");
//		assert(repository.size() == 0);
//		assert(repository.exists("1") == 0);
//	}
//	std::remove("D:\\myTest.db");
//}
//
//void test_SQL_update() {
//	{
//		SQLRepository repository{ "D:\\myTest.db" };
//		repository.add(Movie{ "1", "2", "3", 4, 5 });
//		repository.update("1", "200", "300", 400, 500);
//		auto movie = repository.getData().at(0);
//		assert(movie.title == "1");
//		assert(movie.genre == "200");
//		assert(movie.trailer == "300");
//		assert(movie.yearOfRelease == 400);
//		assert(movie.numberOfLikes == 500);
//	}
//	std::remove("D:\\myTest.db");
//}
//
//void test_SQL_exists() {
//	{
//		SQLRepository repository{ "D:\\myTest.db" };
//		repository.add(Movie{ "1", "2", "3", 4, 5 });
//		assert(repository.exists("1"));
//		assert(!repository.exists("2"));
//	}
//	std::remove("D:\\myTest.db");
//}
//
//void test_SQL_size() {
//	{
//		SQLRepository repository{ "D:\\myTest.db" };
//		assert(repository.size() == 0);
//		repository.add(Movie{ "1", "2", "3", 4, 5 });
//		assert(repository.size() == 1);
//		repository.add(Movie{ "2", "2", "3", 4, 5 });
//		assert(repository.size() == 2);
//	}
//	std::remove("D:\\myTest.db");
//}
//
//void test_SQL_getData() {
//	{
//		SQLRepository repository{ "D:\\myTest.db" };
//		repository.add(Movie{ "1", "2", "3", 4, 5 });
//		repository.add(Movie{ "2", "2", "3", 4, 5 });
//		repository.add(Movie{ "3", "2", "3", 4, 5 });
//		auto movies = repository.getData();
//		assert(movies.size() == 3);
//		auto found = std::find_if(movies.begin(), movies.end(), [](Movie& a) { return a.title == "1"; });
//		assert(found != movies.end());
//		found = std::find_if(movies.begin(), movies.end(), [](Movie& a) { return a.title == "2"; });
//		assert(found != movies.end());
//		found = std::find_if(movies.begin(), movies.end(), [](Movie& a) { return a.title == "3"; });
//		assert(found != movies.end());
//	}
//	std::remove("D:\\myTest.db");
//}

void test_Validator() {
	Movie movie1{ "1", "", "3", 4, 5 };
	Movie movie2{ "1", "2", "3", -4, 5 };
	Movie movie3{ "1", "2", "3", 4, -5 };
	try {
		Validator::validateMovie(movie1);
		assert(false);
	}
	catch (ValidationError& error) {
		assert(true);
	}
	try {
		Validator::validateMovie(movie2);
		assert(false);
	}
	catch (ValidationError& error) {
		assert(true);
	}
	try {
		Validator::validateMovie(movie3);
		assert(false);
	}
	catch (ValidationError& error) {
		assert(true);
	}
}

void test_All() {
	add_valid();
	add_invalid();
	save_valid();
	save_invalid();
	updateController();
	removeController();
	movie_test();
	movie_toString();
	file_write_test();
	utils_isNumber();
	test_HTML_file();
	test_FileRepo_remove();
	test_FileRepo_size();
	test_FileRepo_update();
	test_RepositoryFactory();
	/*test_SQL_add();
	test_SQL_remove();
	test_SQL_update();
	test_SQL_exists();
	test_SQL_getData();
	test_SQL_size();*/
	test_NONTRIVIALFUNCTION();
	test_Validator();
}