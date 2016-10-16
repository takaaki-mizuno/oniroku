# Copyright 2016 Takaaki Mizuno. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""
Oniroku
----

"""

from oniroku.project import Project
from oniroku.git import Git
from oniroku.cocoapods import Cocoapods
from oniroku.replacer import Replacer

__version__ = '0.0.1'


class Oniroku:
    def __init__(self, name, file, directory, config={}):
        self.name = name
        self.directory = directory
        self.project = Project(file, self)
        self.config = config
        self.repo = None

    def execute(self):
        self.repo = Git(self).clone_repo()
        Replacer(self).change_name()
        pod = Cocoapods(self)
        pod.pod_repo_update()
        pod.pod_install()
