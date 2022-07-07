import json


class SettingsService():

    def __init__(self):
        self._properties = {}
        self.settings()

    def settings(self):

        with open('/home/italoco/Repos/ingest-bycicle-data/src/appSettings.json') as jsonFile:
            data = json.load(jsonFile)

            self._properties['host'] = data.get('host')
            self._properties['port'] = data.get('port')
            self._properties['database'] = data.get('database')
            self._properties['user'] = data.get('user')
            self._properties['password'] = data.get('password')


    @property
    def properties(self):
        return self._properties


        



