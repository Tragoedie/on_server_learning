"""
Пример 1.
Рабочая область вывода результатов обследования промышленных агрегатов.
Рабочую область можно представить как несколько окон с линиями, описываюшими форму сигнала, его спектр и кепстр.
Поскольку спектр высчитывается из формы, а кепстр из спектра, то можно составить следующую иерархию:
Линия формы сигнала -> линия спектра -> линия кепстра. Также в иерархию можно включить и линию трендов, которая
будет представлять из себя линию, состоящую из точек с вершинами из значених общих уровней замеров ФС, спектра
или др. Т.е. базовым будет класс линии, которая строится из набора точек либо обработанного.
С другой стороны замеры термограмм имеют абслютно другую структуру данных, и строятся в формате картинки на рабочей
области. При этом линия трендов может строиться, например, по максимальным значениям некоторых термограмм, либо
из набора точек линии Брезенхема, построенной по выбранным двум точкам на термограмме. В таком случае наследование
поломает вывод и общую структуру проекта анализа данных, проще дополнить блок данных виброзамеров блоком данных
термограмм и в зависимости от наличия тех или иных данных обрабатывать данные в по соответсвующему алгоритму.

Пример 2.
Если представить животную иерархию, то можно условно разделить животных на летающих или нет.
Поскольку звери или рептилии летать не умеют, то можно представить в виде животное -> летающее. И дополнить,
например, животное -> летающее -> птица. Вот только сущетсвуют нелетающие птицы, например, пингвины или курицы.
В таком случае целесообразно будет изменить иерархию на животное -> птица -> летающее. Вот только летать умеют
не только птицы, но и, например, насекомые. В таком случае иерархия ломается, и лучше летающих животных выделить как
отдельное состояние: летающее или не летающее.
"""
