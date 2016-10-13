import os
from collections import Counter

def are_files_duplicates(file_path1, file_path2):
    if os.path.getsize(file_path1) == os.path.getsize(file_path2) and \
        os.path.basename(file_path1) == os.path.basename(file_path2):
        return True
    else:
        return False


def get_all_files(start_filepath):
    all_files = [] # (filepath)
    for root, dirs, files in os.walk(start_filepath, topdown=False):
        for current_file in files:
            current_path_of_file = os.path.join(str(root), str(current_file))
            all_files.append(current_path_of_file)
    return all_files

def pretty_print_list(paths):
    were_printed = []
    for path_number, path in enumerate(paths[:-1]):
        if path_number not in were_printed:
            print('File {} is saved in:'.format(os.path.basename(path)))
            does_it_have_a_couple = False
            for other_path_number, other_path in enumerate(paths[path_number+1:]):
                if are_files_duplicates(path, other_path):
                    does_it_have_a_couple = True
                    absolut_number_of_path_in_list = other_path_number + path_number + 1
                    print(other_path)
                    were_printed.append(absolut_number_of_path_in_list)
            if does_it_have_a_couple:
                were_printed.append(path_number)
                print(path)
            print('__________________')


def get_count_filenames_repeats(filepath_folder):
    filepaths_of_all_files = get_all_files(filepath_folder)
    list_of_files_to_remove = []
    all_names = []
    for path in filepaths_of_all_files:
        all_names.append(os.path.basename(path))
    list_of_counts = Counter()
    for name in all_names:
        list_of_counts[name] += 1
    return list_of_counts


if __name__ == '__main__':
    filepath_folder = input('Enter filepath to dir: ')
    #filepath_folder = 'delete'
    count_of_repeats_of_name = get_count_filenames_repeats(filepath_folder)
    filepaths_of_all_files = get_all_files(filepath_folder)
    filepaths_of_repeating_files = []
    for filepath in filepaths_of_all_files:
        if count_of_repeats_of_name[os.path.basename(filepath)] > 1:
            filepaths_of_repeating_files.append(filepath)
    pretty_print_list(filepaths_of_repeating_files)
    

   
