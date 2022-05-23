from balok import Balok
from balok_controller import BalokController
from balok_view import BalokView

shape = Balok(5, 10, 15)
hitung = BalokController()
show = BalokView()

show.show_luas(shape, BalokController)
show.show_keliling(shape, BalokController)
