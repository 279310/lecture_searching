from pathlib import Path
import json


def read_data(file_name, field):
    with open(file_name, "r") as file_obj:
        data = json.load(file_obj)
    with open('sequential.json', "r") as file:
        sequentials = json.load(file)
    if field in sequentials:
        return data[field]
    else:
        return None

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    data = read_data('sequential.json', 'ordered_numbers')
    print(linear_search(sequential_data, 54))
    print(binary_search(data, 64))

def linear_search(sequence, num):
    pos = []
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == num:
            pos.append(sequence[i])
            count+=1
    return {'positions' : pos, 'count' : count}

def binary_search(sequence,num):
    plus = 0
    while len(sequence)>0:
        if num == sequence[int(len(sequence)/2)]:
            return int(len(sequence)/2) + plus
        elif num < sequence[int(len(sequence)/2)]:
            sequence = sequence[0:int(len(sequence)/2)]
        else:
            plus += len(sequence[0:int(len(sequence) / 2)+1:])
            sequence = sequence[int(len(sequence) / 2)+1::]
    return None



if __name__ == "__main__":
    main()
