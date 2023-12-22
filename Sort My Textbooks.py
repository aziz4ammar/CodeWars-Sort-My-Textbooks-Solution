def sorter(textbooks):
    sorted_textbooks = sorted(textbooks, key=lambda x: x.lower())
    return sorted_textbooks