from collections import defaultdict


def book_word_count(file_contents):
        word_count = len(file_contents.split())
        return word_count


def character_count(file_contents):
    lower_words = file_contents.lower()
    counts = defaultdict(int)
    for ch in lower_words:
          counts[ch] += 1
          ch_dict_unsorted = dict(counts)
    return ch_dict_unsorted


def dict_sort(ch_dict_unsorted):
      ch_dict_sorted =[
            {"char": ch, "num": num}
            for ch, num in ch_dict_unsorted.items()
            if ch.isalpha()
      ]
      ch_dict_sorted.sort(key=lambda char: char["num"], reverse=True)
      return ch_dict_sorted