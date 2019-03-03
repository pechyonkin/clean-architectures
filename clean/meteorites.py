from clean import calc
import urllib.request
import json

URL = "https://data.nasa.gov/resource/y77d-th95.json"


class MeteoriteStats:
    def get_data(self) -> list:
        """Get json meteorite data from NASA server

        Returns:
            list -- json data
        """

        with urllib.request.urlopen(URL) as url:
            return json.loads(url.read().decode())

    def average_mass(self, m_data: list) -> float:
        """Calculate average meteorite mass.

        Arguments:
            m_data {list} -- json object of meteorite data

        Returns:
            float -- average meteorite mass
        """

        meteorite_masses = [float(d['mass']) for d in m_data if 'mass' in d]
        return calc.Calc().avg(meteorite_masses)
