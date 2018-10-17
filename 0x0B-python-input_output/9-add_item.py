#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    load = __import__('8-load_from_json_file').load_from_json_file
    save = __import__('7-save_to_json_file').save_to_json_file
    filename = "add_item.json"
    try:
        data = load(filename)
        for i in range(len(argv)):
            if i != 0:
                data.append(argv[i])
        save(data, filename)
    except FileNotFoundError:
        data = []
        for i in range(len(argv)):
            if i != 0:
                data.append(argv[i])
        save(data, filename)
