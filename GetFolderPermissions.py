import os
import csv
import subprocess


def get_folder_permissions():
    # choose a root location that you want to search all directories of
    # omit the final / as it is added later
    csv_save = input("Where would you like to save the csv? (use C: if unsure): ")
    rootdir = input("Enter dir where folders are: ")
    if "\\" not in rootdir:
        file_name = str(rootdir.split("/")[-1])
    else:
        file_name = str(rootdir.split("\\")[-1])

    csv_file = open(csv_save + "/FolderPerms for " + file_name + ".csv", 'w', encoding="UTF8", newline='')
    rootdic = {"Folder Path": f"This is for {file_name}",
               "Permissions": f"Below are permissions for sub folders in {file_name}"}
    fieldnames = ["Folder Path", "Permissions"]
    csv_writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow(rootdic)
    rows = []

    # we only want to find folders in this one root rather than walk through
    # all subdirs so we use scandir
    with os.scandir(path=rootdir) as myroot:
        for folder in myroot:
            if not folder.name.startswith('.') and folder.is_dir():
                # this gets the path of the sub dirs
                subdir = rootdir + "/" + folder.name
                final_str = []
                test_perm = []
                # we need to get permissions for each folder and add it to a list
                output = subprocess.check_output(["icacls", subdir])
                try:
                    encoding = "utf-8"
                    output_str = output.decode(encoding)\
                        .strip("\nSuccessfully processed 1 files; Failed processing 0 files\r")\
                        .split(",")
                # added this because I encountered an error with non utf-8 chars
                except UnicodeDecodeError:
                    encoding = 'ISO-8859–1'
                    output_str = output.decode(encoding)\
                        .strip("\nSuccessfully processed 1 files; Failed processing 0 files\r")\
                        .split(",")
                # print(output_str)
                for x in output_str:
                    # print(x)
                    test_perm.append(x)
                # now the data is there I need to tidy it up because
                # it is all misaligned with random spaces
                my_str = " ".join(test_perm)
                my_str = my_str.strip(subdir).split("\n")
                for x in my_str:
                    final_str.append(x.lstrip())
                # print(final_str)
                my_str = "\n".join(final_str)

                # then we create a dict of path and perms for each subdirectory
                folder_dict = {'Folder Path': subdir, 'Permissions': my_str}
                # add it to our list of rows to be printed
                rows.append(folder_dict)

    # now we can write all the rows to our csv
    csv_writer.writerows(rows)
    csv_file.close()
    return f"Finished getting all folder permissions for {rootdir}"


print(get_folder_permissions())
