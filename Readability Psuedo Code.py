def compute_readability(text):
    total_words = compute_number_of_words(text)
    total_sentences = compute_number_of_sentences(text)
    total_syllables = compute_number_of_syllables(text)
    readability_score = (206.835 - 1.015 * (total_words / total_sentences)
                         - 84.6 * (total_syllables / total_words))

    if readability_score >= 90.0:
        print('Reading level of 5th Grade')
    elif readability_score >= 80.0:
        print('Reading level of 6th Grade')
    elif readability_score >= 70.0:
        print('Reading level of 7th Grade')
    elif readability_score >= 60.0:
        print( 'Reading level  of 8-9th Grade')
    elif readability_score >= 50.0:
        print('Reading level of 10-12th Grade')
    elif readability_score >= 30.0:
        print('Reading Level of College Student')
    else:
        print('Reading level of College Graduate')

    return(readability_score)


DEFINE a function compute_number_of_words passing in text:
    ...
    return number_of_words

DEFINE a function compute_number_of_sentences passing in text:
    ...
    return number_of_sentences


DEFINE a function compute_number_of_syllables passing in text:
    ...
    return number_of_syllables


compute_readability(nytimesarticle)
