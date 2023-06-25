import requests
import geocoder


class GeoLocation:
    """
        Dedicated class to get geolocation of assistant
    """
    def getIp(self) -> str:
        url = 'https://api.ipify.org'  # Serviço para obtenção do endereço IP
        response = requests.get(url)
        ip = response.text
        return ip

    def getGeoPosition(self) -> list[float]:
        g = geocoder.ip(self.getIp())
        return g.latlng
