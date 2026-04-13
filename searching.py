from pathlib import Path
import json


def read_data(file_name, field):
    with open(file_name, "r") as file_obj:
        data = json.load(file_obj)
    with open('sequential.json', "r") as file:
        sequentials = json.load(file)
    if field in sequentials:
        return {field: data}
    else:
        return None

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


def main():
    sequential_data = read_data('sequentials.json', 'unordered_numbers')
    print(sequential_data)


if __name__ == "__main__":
    main()
