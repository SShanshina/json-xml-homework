import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()


def count_length(items, words_len, words_top):
    description_list = list()
    for item in items:
        description_list.append(item.find('description').text)
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
        final_result = '\n'.join(result)
    return final_result


with open('newsafr2.txt', 'w', encoding='utf-8') as f:
    f.write(get_top(root.findall('channel/item'), 6, 10))