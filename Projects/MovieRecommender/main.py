import preprocessing
import os.path as path
import random
import csv


def find_top_five(personalized_array):
    top_five = sorted(range(len(personalized_array)),
                      key=lambda i: personalized_array[i])[-5:]
    top_five.reverse()
    return top_five


def calculate_rating(response, similarity, num_movies):
    personalized_array = [0] * (num_movies + 1)
    for keys, values in response.items():
        for i in xrange(1, num_movies):
            personalized_array[i] += similarity[keys][i] * values
    return personalized_array


def parse_similarity(num_movies):
    similarity = {}
    preprocessed_file = open(
        'Projects/MovieRecommender/preprocessed_data.csv', "r")
    similarity_reader = csv.reader(preprocessed_file)
    for row in similarity_reader:
        similarity[int(row[0])] = map(float, row[1:num_movies + 1])
    preprocessed_file.close()
    return similarity


def random_survey(movies_name, num_movies, number_of_questions):
    n = 0
    response = {}
    while n != number_of_questions:
        mid = random.randint(1, num_movies)
        print("How Much You rate", movies_name[mid],
              "between 1 to 5 (insert -1 if you have not seen it)")
        try:
            num = input()
            if type(num) == int or type(num) == float:
                if num <= 5.0 and num >= 1.0:
                    if mid not in response:
                        n += 1
                    response[mid] = num
                elif num != -1:
                    print "please rate between 1 to 5"
                else:
                    print "Here's another option"
            else:
                print "please insert integer of float between 1 to 5"
        except:
            print "Insert Integers Only"
            print "Now Fill this survey correctly!!!"
    return response


def main():
    similarity = None
    number_of_questions = 10
    movies_name = None
    if path.isfile('Projects/MovieRecommender/preprocessed_data.csv') is False:
        print "preprocessing data Hold on Please..."
        print "It'll take  few minutes"
        movies_name, similarity = preprocessing.preprocess()
    if movies_name is None:
        movies_name = preprocessing.get_movies_name()
    num_movies = len(movies_name)
    user_response = random_survey(movies_name, num_movies, number_of_questions)
    if similarity is None:
        similarity = parse_similarity(num_movies)
    personalized_array = calculate_rating(
        user_response, similarity, num_movies)
    top_five = find_top_five(personalized_array)
    print "Suggested Movies Are:"
    for i in xrange(5):
        print i+1, movies_name[top_five[i]]


if __name__ == '__main__':
    main()
