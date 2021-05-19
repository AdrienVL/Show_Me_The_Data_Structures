
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    filesList = []

        # Iterate through entire directory
            #If isfile - file ends with suffix - append to filesList else do nothing
            #if is directory - Join paths and call function recursively. --->> recursively


    content = os.listdir(path)

    # for item in content:
    #     if os.path.isdir("{}/{}".format(path,item)):
    #         #     print(suffix,os.path.join(path,item))
    #         #     sub_compound = find_files(suffix,os.path.join(path,item))

    #         new_path = "{}/{}".format(path,item)
    #         print(new_path)
 
    #         directory_list.append(new_path)
    #         sub_compound = find_files(suffix,new_path)

    #         print(sub_compound)

    for item in content:
        if os.path.isfile("{}/{}".format(path,item)):
            if "{}/{}".format(path,item).endswith(suffix):
                file_path = ("{}/{}".format(path,item))
                filesList.append(file_path)
        elif os.path.isdir("{}/{}".format(path,item)):
            # print(suffix,os.path.join(path,item))
            new_path = "{}/{}".format(path,item)

            sub_compound = find_files(suffix,new_path)
            print("sub_compound:{}".format(sub_compound))

            for file in sub_compound:
                print("file:{}".format(file))
                filesList.append(file)
    

                
    # ./testdir
    # ./testdir/subdir1
    # ./testdir/subdir1/a.c
    # ./testdir/subdir1/a.h
    # ./testdir/subdir2
    # ./testdir/subdir2/.gitkeep
    # ./testdir/subdir3
    # ./testdir/subdir3/subsubdir1
    # ./testdir/subdir3/subsubdir1/b.c
    # ./testdir/subdir3/subsubdir1/b.h
    # ./testdir/subdir4
    # ./testdir/subdir4/.gitkeep
    # ./testdir/subdir5
    # ./testdir/subdir5/a.c
    # ./testdir/subdir5/a.h
    # ./testdir/t1.c
    # ./testdir/t1.h


    # Is directory
    # print (path1[0])
    # print(os.path.join(path,path1[0]))

    # # Let us check if this file is indeed a file!
    # print (os.path.isfile("./ex.py"))

    # #Does the file end with .py?
    # print ("./ex.py".endswith(".py"))


    return filesList

print(find_files('.h','./testdir'))
