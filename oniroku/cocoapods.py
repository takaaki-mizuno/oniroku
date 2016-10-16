# -*- coding: utf-8 -*-

import subprocess


class Cocoapods:
    def __init__(self, oniroku):
        self.repo = oniroku.repo

    def pod_install(self):
        cmd = "cd " + self.repo + "; pod install"
        subprocess.call(cmd, shell=True)

    def pod_repo_update(self):
        cmd = "cd " + self.repo + ";pod repo update"
        subprocess.call(cmd, shell=True)
