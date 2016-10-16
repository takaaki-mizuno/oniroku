# -*- coding: utf-8 -*-

import json


class Project():
    def __init__(self, file, oniroku):
        self.project = None
        self.read_file(file)

    def read_file(self, file):
        with open(file, 'r') as f:
            self.project = json.load(f)

    def get(self, name, default=None):
        if name in self.project:
            return self.project[name]
        return default
