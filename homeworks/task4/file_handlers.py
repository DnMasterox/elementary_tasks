__author__ = 'nshumakov'


class FileParser(object):
    def __init__(self, path_to_file):
        self.path = path_to_file


class FileStringFinder(FileParser):
    def __init__(self, path_to_file, need_str):
        FileParser.__init__(self, path_to_file)
        self.__path_to_file = path_to_file
        self.__need_str = need_str
        self.__result = 0

    def print_occurrences(self) -> None:
        self.__get_occurrences()
        print(self.__result)

    def __get_occurrences(self) -> []:
        self.__result = 0
        for line in open(self.__path_to_file):
            if self.__need_str in line:
                self.__result += 1
            else:
                pass
        return self.__result


class FileStringReplacer(FileParser):
    def __init__(self, path_to_file, need_str, replace_str):
        super().__init__(path_to_file)
        self.__path_to_file = path_to_file
        self.__need_str = need_str
        self.__replace_str = replace_str
        self.__try_to_replace()

    def __try_to_replace(self) -> None:
        with open(self.__path_to_file, 'r') as file:
            temp = file.read()
            if self.__need_str in temp:
                data = temp.replace(self.__need_str, self.__replace_str)
                with open(self.__path_to_file, 'w') as file:
                    file.write(data)
                    print('Replacing {} to {}'.format(self.__need_str,
                                                      self.__replace_str) +
                          ' was successfully made')
            else:
                print('Replacing failed')
