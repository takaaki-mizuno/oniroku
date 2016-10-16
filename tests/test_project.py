import unittest
import os
from oniroku.project import Project


class TestProject(unittest.TestCase):
    def test_add_three(self):
        file = os.path.dirname(os.path.realpath(__file__)) + '/data/project_sample.json'
        project = Project(file, None)
        self.assertEqual(project.get('projectName'), 'Sample')
