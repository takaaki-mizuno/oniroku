# -*- coding: utf-8 -*-

import os


class Replacer:
    def __init__(self, oniroku):
        self.repo = oniroku.repo
        self.name = oniroku.name

    def change_name(self):
        self._change_name(self.repo)

    def _change_name(self, start_directory):
        for directory, subdirectories, files in os.walk(start_directory):
            for file_name in files:
                self.replace(os.path.join(directory, file_name))
            for subdirectory in subdirectories:
                if subdirectory == '.git':
                    continue
                new_subdirectory = subdirectory.replace("oniroku-template", self.name)
                if new_subdirectory != subdirectory:
                    os.rename(os.path.join(directory, subdirectory), os.path.join(directory, new_subdirectory))
                self._change_name(os.path.join(directory, new_subdirectory))

    def replace(self, file):
        try:
            print("REPLACE: " + file);
            f = open(file, 'r')
            data = f.read()
            f.close()

            new_file = file.replace("oniroku-template", self.name)
            os.remove(file)

            new_data = data.replace("oniroku-template", self.name)
            f = open(new_file, 'w')
            f.write(new_data)
            f.close()
        except:
            print("ERROR");