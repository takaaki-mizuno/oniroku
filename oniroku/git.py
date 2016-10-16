# -*- coding: utf-8 -*-

from git import Repo
import os


class Git:
    def __init__(self, oniroku):
        self.repos = self.get_template_repo()
        self.directory = oniroku.directory
        self.name = oniroku.name

    def get_template_repo(self):
        return "git@github.com:takaaki-mizuno/oniroku-template-tab.git"

    def clone_repo(self):
        repo_directory = os.path.join(self.directory, self.name)
        Repo.clone_from(self.repos, repo_directory, branch='master')
        return repo_directory
