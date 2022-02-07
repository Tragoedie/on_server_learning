# Для проверки виброданных, полученных с датчиков был реализован класс CWaveFormLine, который выводит данные (форму
# сигнала) в виде набора точек, созданных в единую линию. После возникает необходимость в выводе сигналов в виде
# спектов и кепстров, вывод столбчатых диаграмм, линий трендов. Все эти линии будут иметь общую структуру (массив с
# точками), набор обших методов (отрисовка линии, вывод пояснения), которые можно будет объединить в один родительский
# класс CGraphLine, а в дочерних классах определять специфические методы (метод отрисовки столбчатой диаграммы, расчёт
# вывода линии формы сигнала)
# В одной из версий были добавлены замеры XYZ, которые выводятся в трёхмерной плоскости. Слегка спустя были добавлены
# замеры Орбит, которые также выводились в трёхмерной плоскости. Для остальных замеров была реализована возможность
# вывода линий форм сигнала и др. в трёхмерной плоскости, расположенные параллельно друг другу на Z-оси. Для унификации
# изменений был добавлен промежуточный класс CGraphAxis, который позволял выводить как XY-ось, так и XYZ-оси. Объекты
# осей были добавлены как одна из составляющих частей CGraphArea.
