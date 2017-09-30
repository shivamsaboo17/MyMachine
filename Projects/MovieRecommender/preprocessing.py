import csv
import math


class movie():

    def __init__(self, name, uid=[], rating=[]):
        self.name = name
        self.uid = uid
        self.rating = rating

    def add_user(self, uid, rating):
        self.uid.append(uid)
        self.rating.append(rating)


def pearson_score(i, j, movies):
    n = 0
    sum1 = 0
    sum2 = 0
    sumsqr1 = 0
    sumsqr2 = 0
    psum = 0
    for usr in movies[i].uid:
        if usr in movies[j].uid:
            n += 1
            indexi = movies[i].uid.index(usr)
            indexj = movies[j].uid.index(usr)
            sum1 += movies[i].rating[indexi]
            sum2 += movies[j].rating[indexj]
            sumsqr1 += movies[i].rating[indexi] ** 2
            sumsqr2 += movies[j].rating[indexj] ** 2
            psum += movies[i].rating[indexi] * movies[j].rating[indexj]

    if n == 0:
        return 0
    else:
        num = n * psum - sum1*sum2
        den = math.sqrt((n * sumsqr1 - sum1 ** 2) * (n * sumsqr2 - sum2 ** 2))
        if den == 0:
            return 0
        return float(num)/den


def save_similarity(similarity):
    new_file = open("Projects/MovieRecommender/preprocessed_data.csv", "w")
    writer = csv.writer(new_file)
    for i in similarity:
        row = [i]
        row += [similarity[i][j] for j in similarity[i]]
        writer.writerow(row)
    new_file.close()


def get_similarity(similarity, movies):
    for i in movies:
        similarity[i] = {}
        for j in movies:
            if i != j:
                similarity[i][j] = pearson_score(i, j, movies)
            else:
                similarity[i][j] = 1
    return similarity


def fill_movies(movies):
    movie_file = open('Projects/MovieRecommender/MovieData/movies.csv', "r")
    movie_reader = csv.reader(movie_file)
    for row in movie_reader:
        movies[int(row[0])] = row[1]
    movie_file.close()
    return movies


def preprocess():
    movies_name = {}
    movies_name = fill_movies(movies_name)
    user_file = open('Projects/MovieRecommender/MovieData/rating.csv', "r")
    user_reader = csv.reader(user_file)
    movies = {}
    for row in user_reader:
        if int(row[1]) in movies:
            movies[int(row[1])].add_user(int(row[0]), float(row[2]))
        else:
            movies[int(row[1])] = movie(movies_name[int(row[1])],
                                        [int(row[0])], [float(row[2])])
    user_file.close()
    similarity = {}
    similarity = get_similarity(similarity, movies)
    save_similarity(similarity)
    return (movies_name, similarity)


def get_movies_name():
    movies_name = {}
    return fill_movies(movies_name)
