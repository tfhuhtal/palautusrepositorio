from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deserialized = tomli.loads(content)

        return Project(deserialized["tool"]["poetry"]["name"],
                    deserialized["tool"]["poetry"]["description"],
                    deserialized["tool"]["poetry"]["dependencies"], 
                    deserialized["tool"]["poetry"]["group"]["dev"]["dependencies"])
