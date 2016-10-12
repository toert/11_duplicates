import os


def are_files_duplicates(file_path1, file_path2):
    if os.path.getsize(file_path1) == os.path.getsize(file_path2) and \
        os.path.basename(file_path1) == os.path.basename(file_path2):
        return True
    else:
        return False


def get_all_files(start_filepath):
    all_files = [] # (filepath, filename, size)
    for root, dirs, files in os.walk(start_filepath, topdown=False):
        for i in range(len(files)):
            path_of_file = str(root) + '\\' + str(files[i])
            current_file = (path_of_file, str(files[i]), \
                os.path.getsize(path_of_file))
            all_files.append(current_file)
    return all_files


if __name__ == '__main__':
    filepath_folder = input('Enter filepath to dir: ')
    data_about_files = get_all_files(filepath_folder)
    list_of_files_to_remove = []
    for current_file in data_about_files[:-1]: #finding_couples_of_same_files
        j = i + 1
        while (j < len(data_about_files)):
            if are_files_duplicates(data_about_files[i][0], \
                data_about_files[j][0]):
                if i not in list_of_files_to_remove:
                    list_of_files_to_remove.append(i)
                if j not in list_of_files_to_remove:
                    list_of_files_to_remove.append(j)
                
            j = j + 1
    print('Same files are:')
    for file in list_of_files_to_remove:
        print(data_about_files[file][0])

            

   
