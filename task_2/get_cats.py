def get_cats_info(path):
    cats = []

    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            try:
                cat = {'id': parts[0], 'name': parts[1], 'age': parts[2]}
                cats.append(cat)
            except ValueError:
                continue

    return cats
