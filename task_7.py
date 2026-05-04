types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def unique_list(lst):
    seen = []
    result = []
    for item in lst:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

def tickets_by_type_no_set(types_dict, tickets_dict):
    assigned = []  # список уже назначенных тикетов
    result = {}
    keys = list(types_dict.keys())
    keys.sort()
    for level in keys:
        name = types_dict[level]
        level_tickets = tickets_dict.get(level, [])
        uniq = unique_list(level_tickets)

        filtered = []
        for t in uniq:
            if t not in assigned:
                filtered.append(t)
                assigned.append(t)

        result[name] = filtered
    return result