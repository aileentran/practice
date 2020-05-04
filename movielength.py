"""
Peeps watch 2 movies on flights
Pick 2 movies that are the exact length of the flight length

input: flight length (min), list of ints (movie length in min)
output: boolean - true (2 movies of right length), false otherwise

notes:
-users will watch 2 DIFFERENT movies
-optimize for runtime over memory

thoughts:
first make the dictionary 
sort ints from shortest to longest?? 
make an empty dictionary: movie length (key), counter for movie (num)
loop through list of movies movie[i] += 1

loop through the list of movie lengths(?)
dict[item] -= 1
if flight - item = key for next movie EXISTS
return true 
else it just keeps going 

outside loop
return false 


"""

def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    # movie_lengths.sort()
    movies = {}
    for movie in movie_lengths:
    	if movie not in movies:
    		movies[movie] = 1
    	else:
    		movies[movie] += 1

    for movie in movie_lengths:
    	movies[movie] -= 1
    	second_movie = flight_length - movie

    	if (second_movie in movies and movies[second_movie] > 0):
    		return True

    return False