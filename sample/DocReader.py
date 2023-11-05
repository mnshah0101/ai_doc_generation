import os


class DocReader:
    def __init__(self, path):
        if (path == None or path.strip() == ''):
            raise ValueError('path is required')
        self.path = path
        return_files = []

        for root, dirs, files in os.walk(path):
            for file in files:
                return_files.append(os.path.join(root, file))

        # Filter the files to only include python files
        python_files = [file for file in return_files if file.endswith(".py")]

        # Save the paths of the python files
        python_file_paths = [os.path.join(path, file)
                             for file in python_files]

        self.python_file_paths = python_file_paths

    def read(self):
        returnString = ""
        for path in self.python_file_paths:
            returnString += self.read_file(path) + "\n"

        listReturn = returnString.split()

        if (len(listReturn) < 5000):
            return ['raw', returnString]
        else:
            return ['formatted', self.format_string(returnString)]

    def read_file(self, path):
        with open(path, 'r') as f:
            data = f.read()
        return data

    def format_string(self, input_string):
        unformat_list = input_string.split('\n')

        format_list = [
            line for line in unformat_list if 'def' or '#' or 'class' or '=' in line]

        return_string = "\n".join(format_list)

        return return_string
