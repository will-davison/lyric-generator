import pronouncing
import random
from rhymetest import bestChoice


def replace_words_from_song():
    with open('BillyOcean.txt') as f:
        lines = [line for line in f.readlines()]

    # with open('oscar-wilde-lord-arthur-savile-s-crime-and-other-stories.txt') as f2:
    #     lines_from_book = [line for line in f2.readlines()]

    final_list = []
    for line in lines:
        list_of_words = [pronouncing.rhymes(word) for word in line.split(' ')]
        line_as_array = line.split(' ')
        dump_list = []
        dump_list_2 = []
        dump_list_3 = []
        dump_list_4 = []
        # print(line_as_array)
        for i,words in enumerate(list_of_words):
            try:
                if i % 4 == 0 and len(words):
                    dump_list.append(random.choice(words))
                    dump_list_2.append(random.choice(words))
                    dump_list_3.append(random.choice(words))
                    dump_list_4.append(random.choice(words))
                elif i % 3 == 0 and len(words): 
                    dump_list.append(random.choice(words))
                    dump_list_2.append(random.choice(words))
                    dump_list_3.append(random.choice(words))
                    dump_list_4.append(random.choice(words))
                else:
                    dump_list.append(line_as_array[i])
                    dump_list_2.append(line_as_array[i])
                    dump_list_3.append(line_as_array[i])
                    dump_list_4.append(line_as_array[i])
            except:
                pass
        
        if len(line) == 1: continue
        
        best_word = bestChoice(
            line,
            [' '.join(dump_list), ' '.join(dump_list_2), ' '.join(dump_list_3), ' '.join(dump_list_4)],
            1,
            0.1
        )
        final_list.append(best_word)
    return final_list


        

print(' '.join(replace_words_from_song()))