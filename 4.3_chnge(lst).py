def change(lst):
    last_element = lst.pop()
    first_element = lst.pop(0)
    lst.append(first_element)
    lst.insert(0, last_element)
    return lst
print(change(['т', 'а', 'м', 'о', 'л', 'е', 'с',]))