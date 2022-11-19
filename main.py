import pronouncing
import random


def replace_words_from_song():
    with open('BillyOcean.txt') as f:
        lines = [line for line in f.readlines()]

    # with open('oscar-wilde-lord-arthur-savile-s-crime-and-other-stories.txt') as f2:
        # lines_from_book = [line for line in f2.readlines()]
        # print(lines_from_book)

    final_list = []
    for line in lines:
        list_of_words = [pronouncing.rhymes(word) for word in line.split(' ')]
        line_as_array = line.split(' ')
        dump_list = []
        # print(line_as_array)
        for i,words in enumerate(list_of_words):
            try:
                if i % 4 == 0 and len(words):
                    random_word = random.choice(words)
                    dump_list.append(random_word)
                else: 
                    dump_list.append(line_as_array[i])
            except:
                pass
        final_list.append(' '.join(dump_list))
    return final_list


        

final_results = []
final_results.append(replace_words_from_song())
final_results.append(replace_words_from_song())
final_results.append(replace_words_from_song())

        
