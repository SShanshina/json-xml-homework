import json
from collections import Counter

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)


def count_length(items, words_len, words_top):
    description_list = list()
    for item in items:
        description_list.append(item['description'])
    big_str = ' '.join(description_list)
    words_list = big_str.split(' ')
    long_words = list()
    for word in words_list:
        if len(word) > words_len:
            long_words.append(word)
    words_len_list = Counter(long_words).most_common(words_top)
    return words_len_list


def get_top(items, words_len, words_top):
    result = list()
    for i, word_list in enumerate(count_length(items, words_len, words_top)):
        if i < words_top:
            result.append(f'{i + 1}. {word_list[0].capitalize()}: {word_list[1]}')
    return result


with open('newsafr2.json', 'w', encoding='utf-8') as f:
    json_data = json.dump(get_top(json_data['rss']['channel']['items'], 6, 10), f, ensure_ascii=False, indent=2)