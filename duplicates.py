import os
from collections import Counter
from collections import defaultdict


def are_files_duplicates(file_path1, file_path2):
    name1 = os.path.splitext(os.path.basename(file_path1))[0]
    name2 = os.path.splitext(os.path.basename(file_path2))[0]
    return bool(os.path.getsize(file_path1) == os.path.getsize(file_path2) and \
                ((name1[:-4] == name2) or (name1 == name2[:-4]) or (name1 == name2)))


def are_files_copies(file_path1, file_path2):
    name1 = os.path.splitext(os.path.basename(file_path1))[0]
    name2 = os.path.splitext(os.path.basename(file_path2))[0]
    return bool(os.path.getsize(file_path1) == os.path.getsize(file_path2) and \
                ((name1[:-4] == name2) or (name1 == name2[:-4])))


def get_all_files(start_filepath):
    all_files = []
    for root, dirs, files in os.walk(start_filepath, topdown=False):
        for current_file in files:
            current_path_of_file = os.path.join(str(root), str(current_file))
            all_files.append(current_path_of_file)
    return all_files


def get_dict_with_sizes(filepath):
    dict = {}
    for path in filepath:
        dict[path] = os.path.getsize(path)
    return dict


def get_dict_of_copies(paths, mode=1):
    """
    mode = 1  => get all copies
    mode = 2 => get copies like 17.txt, 17 (1).txt, 17 (2).txt, etc
    """
    struct_files = defaultdict(list)
    only_repeating = defaultdict(list)
    sizes = get_dict_with_sizes(paths)
    were_saved = []
    number_repeat = -1
    for path_number, path in enumerate(paths[:-1]): #because the last will be compared with all other files
        if path not in were_saved:
            number_repeat = number_repeat + 1
            struct_files[number_repeat].append(path)
            does_it_have_a_couple = False
            for other_path_number, other_path in enumerate\
(list(filter(lambda filepath: sizes[filepath] == sizes[path] , paths[path_number + 1:]))):
                if mode == 1:
                    if are_files_duplicates(path, other_path):
                        does_it_have_a_couple = True
                        struct_files[number_repeat].append(other_path)
                        were_saved.append(other_path)
                if mode == 2:
                    if are_files_copies(path, other_path):
                        does_it_have_a_couple = True
                        struct_files[number_repeat].append(other_path)
                        were_saved.append(other_path)
            if does_it_have_a_couple:
                were_saved.append(path)
    for key in struct_files:
        if len(struct_files[key]) > 1:
            only_repeating[key] = struct_files[key]
    return only_repeating


def get_list_repeating_files(filepath_folder):
    filepaths_of_all_files = get_all_files(filepath_folder)
    all_names = []
    for path in filepaths_of_all_files:
        all_names.append(os.path.basename(path))
    list_of_counts = Counter(all_names)
    list_of_counts.most_common()
    return list(filter(lambda filepath: list_of_counts[os.path.basename(filepath)] > 1\
                       , filepaths_of_all_files))


def get_sum_size(dict):
    sum = 0
    for key in dict:
        sum = sum + (os.path.getsize(dict[key][0])*len(dict[key]))
    inMb = float(sum / (1024*1024))
    return int(inMb)


if __name__ == '__main__':
    filepath_folder = input('Enter filepath to dir: ')
    filepaths = get_all_files(filepath_folder)
    repeating_files = get_dict_of_copies(filepaths,1)
    for key in repeating_files:
        print('File {} is saved in: '.format(os.path.basename(repeating_files[key][0])))
        for path in repeating_files[key]:
            print(path)
