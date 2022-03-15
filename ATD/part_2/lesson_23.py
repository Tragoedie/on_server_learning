# Возьмём за пример реализацию оружия из игры Cyperpunk 2077. Для удобства примера объединю показатели умного и ЭМ-оружия.
# Умным оружием можно воспользоваться только персонажи, с установленным имплантом Smartlink (предусловие: наличие импланта)
# ЭМ-оружие обладает способностью "заряжания" мощи оружия.
# Наследуемся от этого класса в новый: Высокоточное оружие. Им можно пользоваться вне зависимости от наличия имплантов
# (ослабление предусловия), но отсуствует возможность накопления заряда, т.е. выстрел происходит моментально
# (усиление постусловия).
# В случае обратного порядка наследования возникает проблема с использованием полиморфных объектов. Так появляется
# вероятность того, что умное оружие попадёт в руки персонажу без нужного импланта (усиление предусловия).
# Также при неправильной настройке может возникнуть баг "бесконечной зарядки" (ослабление постусловия).