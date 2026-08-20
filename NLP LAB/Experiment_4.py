def pluralize(noun):
    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    elif noun.endswith('f'):
        return noun[:-1] + 'ves'
    elif noun.endswith('fe'):
        return noun[:-2] + 'ves'
    else:
        return noun + 's'

nouns = ["cat", "bus", "box", "city", "leaf", "knife", "church", "boy", "dog", "wolf"]

print(f"{'Singular':<12}{'Plural':<12}")
for noun in nouns:
    print(f"{noun:<12}{pluralize(noun):<12}")
