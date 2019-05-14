#include "Validator.h"

bool Validator::validateMovie(const Movie & movie)
{
	if (movie.numberOfLikes < 0 || movie.yearOfRelease < 0 || movie.title.empty() || movie.genre.empty() || movie.trailer.empty())
		throw ValidationError("Movie not valid!");
	return true;
}