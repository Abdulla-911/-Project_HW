# processing.py

from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Список словарей, каждый из которых содержит ключ 'state'
        state: Значение для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        List[Dict[str, Any]]: Новый список, содержащий только словари
                              с указанным значением state

    Examples:
        >>> transactions = [
        ...     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        ...     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ...     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        ...     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ... ]
        >>> filter_by_state(transactions)
        [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

        >>> filter_by_state(transactions, 'CANCELED')
        [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    """
    # Создаём новый список, содержащий только словари с нужным значением state
    filtered_list = []

    for item in data:
        # Проверяем, существует ли ключ 'state' и соответствует ли он значению
        if item.get('state') == state:
            filtered_list.append(item)

    return filtered_list


from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Список словарей, содержащих ключ 'state'
        state: Значение для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        List[Dict[str, Any]]: Новый список словарей с указанным значением state
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    Args:
        data: Список словарей, содержащих ключ 'date' с датой в ISO формате
        descending: Порядок сортировки. True - убывание (новые сначала),
                   False - возрастание (старые сначала). По умолчанию True

    Returns:
        List[Dict[str, Any]]: Новый отсортированный список словарей

    Examples:
        >>> transactions = [
        ...     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        ...     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ...     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        ...     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ... ]
        >>> sort_by_date(transactions)
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    """
    # Сортируем список по ключу 'date'
    # Так как даты в ISO формате, их можно сравнивать как строки
    return sorted(data, key=lambda x: x.get('date', ''), reverse=descending)