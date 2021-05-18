
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

    if path is False:
        filesList.append()
    else:

        # Iterate through entire directory
            #If isfile - file ends with suffix - append to filesList else do nothing
            #if is directory - Join paths and call function recursively. --->> recursively

    

        content = os.listdir(path)
        for item in content:
            # print(item)
            if os.path.isfile("{}/{}".format(path,item)):
                if "{}/{}".format(path,item).endswith(suffix):
                    file_path = ("{}/{}".format(path,item))
                    filesList.append(file_path)
            elif os.path.isdir("{}/{}".format(path,item)):
                find_files(suffix,os.path.join(path,item))


    #Is directory
    # print (path1[0])
    # print(os.path.join(path,path1[0]))

    # # Let us check if this file is indeed a file!
    # print (os.path.isfile("./ex.py"))

    # #Does the file end with .py?
    # print ("./ex.py".endswith(".py"))


    return filesList

print(find_files('.c','./testdir'))
