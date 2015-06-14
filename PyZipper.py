from ZipperUtil.DirectoryUtil import DirectoryUtil


def main():
    test_dir = "C:\TestDir"
    directory_util = DirectoryUtil(test_dir)
    for f in directory_util.list_file_names():
        print f

    for f in directory_util.list_full_file_names():
        print f


if __name__ == "__main__":
    main()
