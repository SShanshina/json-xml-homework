import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()


def count_length(items):
    description_list = list()
    for item in items:
        description_list.append(item.find('description').text)
    big_str = ' '.join(description_list)
    words_list = big_str.split(' ')
    long_words = list()
    for word in words_list:
        if len(word) > 6:
            long_words.append(word)
    words_len_dict = Counter(long_words)
    return words_len_dict


def sort_list(items):
    words_list = list()
    for word, length in count_length(items).items():
        word_list = [word, length]
        words_list.append(word_list)
    sort_el_index = 1

    def sort_by_el(i):
        return i[sort_el_index]
    words_list = sorted(words_list, key=sort_by_el)
    words_list = list(reversed(words_list))
    return words_list


def get_top_10(items):
    result = list()
    for i, word_list in enumerate(sort_list(items)):
        if i < 10:
            result.append(f'{i + 1}. {word_list[0].capitalize()}: {word_list[1]}')
        final_result = '\n'.join(result)
    return final_result


with open('newsafr2.txt', 'w', encoding='utf-8') as f:
    f.write(get_top_10(root.findall('channel/item')))