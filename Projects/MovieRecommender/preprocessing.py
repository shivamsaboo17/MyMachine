import csv
import math


class movie():
    '''
    Movie class contain name of movie
    It also contain users like that rated that movie
    And also their respective rating
    '''
    def __init__(self, name, uid, rating):
        self.name = name
        self.uid = uid
        self.rating = rating

    def add_user(self, uid, rating):
        self.uid.append(uid)
        self.rating.append(rating)


def pearson_score(i, j, movies):
    '''
    calculate pearson score between two movies
    :param i: id of 1st movie
    :param j: id of 2nd movie
    :param movies: array whose each element is an object of movie
    :return: returns pearson score b/w ith and jth movie
    '''
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
    '''
    save similarity matrix so we don't have to calculate it always
    :param similarity: 2D similarity dict-matrix
    '''
    new_file = open("Projects/MovieRecommender/preprocessed_data.csv", "w")
    writer = csv.writer(new_file)
    for i in similarity:
        row = [i]
        row += [similarity[i][j] for j in similarity[i]]
        writer.writerow(row)
    new_file.close()


def get_similarity(similarity, movies):
    '''
    Get similarity matrix
    :param similarity: empty simlarity matrix
    :param movies: array whose each element is an object of movie
    :return: returns similarity matrix
    '''
    for i in movies:
        similarity[i] = {}
        for j in movies:
            if i != j:
                similarity[i][j] = pearson_score(i, j, movies)
            else:
                similarity[i][j] = 1
    return similarity


def fill_movies(movies):
    '''
    fill movies dict from movies.csv
    :param movies: empty dict which will contain movies name
    :return: return filled movies array
    '''
    movie_file = open('Projects/MovieRecommender/MovieData/movies.csv', "r")
    movie_reader = csv.reader(movie_file)
    for row in movie_reader:
        movies[int(row[0])] = row[1]
    movie_file.close()
    return movies


def preprocess():
    '''
    execute if preprocessed_data.csv is not process
    returns movies_name  and similarity array
    '''
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
    '''
    return movies_name array
    '''
    movies_name = {}
    return fill_movies(movies_name)
