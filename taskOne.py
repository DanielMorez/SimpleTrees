
def flatten(dictionary: dict, prefix: str = ''):
    temp_dict = dict()
    for key, value in dictionary.items():
        # Проверка вложенность словаря
        if isinstance(value, dict):
            temp_dict.update(
                flatten(value, f'{prefix}{key}.')
            )
        # Базовый случай
        else:
            temp_dict[f'{prefix}{key}'] = value

    return temp_dict

if __name__ == '__main__':
    # Test 1
    d = {
        "a": 5,
        "b": 6,
        "c": {
            "f": 9,
            "g": {
                "m": 17,
                "n": 3
            }
        }
    }
    print("d = {")
    for key, value in flatten(d).items():
        print(f'    "{key}": "{value}",')
    print("}")