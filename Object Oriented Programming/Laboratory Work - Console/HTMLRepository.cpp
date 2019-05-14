#include "HTMLRepository.h"

HTMLRepository::HTMLRepository(std::string name)
{
	fileName = name;
}

void HTMLRepository::display() {
	this->writeToFile();
	//ShellExecuteA(NULL, NULL, "chrome.exe", fileName.c_str(), NULL, SW_SHOWMAXIMIZED);
}

void HTMLRepository::writeToFile() {
	std::ofstream outFile(fileName);
	outFile << "<!DOCTYPE html>" << std::endl;
	outFile << "<html>" << std::endl;
	outFile << "<head><title>Playlist</title></head>" << std::endl;
	outFile << "<body style=\"background-color:powderblue;\"><table border=\"1\">" << std::endl;

	outFile << "<tr>" << std::endl;
	outFile << "<td>Title</td>" << std::endl;
	outFile << "<td>Genre</td>" << std::endl;
	outFile << "<td>Year</td>" << std::endl;
	outFile << "<td>NrLikes</td>" << std::endl;
	outFile << "<td>Link</td>" << std::endl;
	outFile << "</tr>" << std::endl;

	for (const auto& movie : vector) {
		outFile << "<tr>" << std::endl;
		outFile << "<td>" << movie.title << "</td>" << std::endl;
		outFile << "<td>" << movie.genre << "</td>" << std::endl;
		outFile << "<td>" << movie.yearOfRelease << "</td>" << std::endl;
		outFile << "<td>" << movie.numberOfLikes << "</td>" << std::endl;
		outFile << "<td>" << movie.trailer << "</td>" << std::endl;
		outFile << "</tr>" << std::endl;
	}

	outFile << "</table>" << std::endl;
	outFile << "</body>" << std::endl;
	outFile << "</html>" << std::endl;
	outFile.close();
}