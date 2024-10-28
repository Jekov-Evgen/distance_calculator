from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from Style.style import CONST_MESSAGE_BOX

icon = 'Image\icon.jpg'

def distance_calculation(starting_city, final_city, err):
    geolocator = Nominatim(user_agent="geo_calculator")

    try:
        location_start = geolocator.geocode(starting_city)
        location_end = geolocator.geocode(final_city)

        if location_start is None or location_end is None:
            err = QMessageBox()
            err.setWindowIcon(QIcon(icon))
            err.setStyleSheet(CONST_MESSAGE_BOX)
            err.setWindowTitle("Ошибка")
            err.setText("Указанные вами города не найдены")
            err.show()
            return None

        coords_start = (location_start.latitude, location_start.longitude)
        coords_end = (location_end.latitude, location_end.longitude)

        ds = geodesic(coords_start, coords_end).kilometers
        return ds

    except Exception as e:
        err = QMessageBox()
        err.setWindowIcon(QIcon(icon))
        err.setStyleSheet(CONST_MESSAGE_BOX)
        err.setWindowTitle("Ошибка")
        err.setText(f"Произошла ошибка: {str(e)}")
        err.show()
        return None

def fuel_consumption_calculation(consumption : int, distance : int):
    return (consumption * distance) / 100