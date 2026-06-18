movies = {
    "Avengers": [5, 4, 5, 4],
    "Inception": [5, 5, 4, 5],
    "Titanic": [3, 4, 4, 3],
    "Interstellar": [5, 5, 5, 4]
}

average_ratings = {}

for movie, ratings in movies.items():
    average_ratings[movie] = sum(ratings) / len(ratings)

sorted_movies = sorted(
    average_ratings.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Recommended Movies:\n")

for movie, rating in sorted_movies:
    print(f"{movie} - Average Rating: {rating:.2f}")
