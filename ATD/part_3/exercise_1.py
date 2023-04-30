Задание 1.

Составьте предварительное, самое общее, словесное описание системы, которую вы хотите сделать.
Придерживаясь принципов модульности, определите в ней 5-7 наиболее общих сущностей (потенциальных АТД),
пока кратко и неформально их опишите.

Укажите, что делает в системе каждая такая сущность, стараясь, чтобы из этого множества
формулировок "кто что делает" была бы хорошо понятна и общая идея работы системы в целом.


DateTime - ДатаВремя.
Сущность, хранящая дату и время.

AlarmClock - Будильник
Задание времени оповещения, воспроизведение звукового сигнала при наступлении события,
отключение/отложение оповещения.

Timer - Таймер
Задание конечного времени отсчёта либо интервала, отсчёт времени и выдача оповещения о срабатывании точки остановки.

Stopwatch - Секундомер
Запуск отсчёта времени и запись контрольной точки (остановки) по указанию пользователя,
вывод временного(-ых) промежутка(-ов)

Note - Заметка
Содержит в себе текстовую информацию о пользовательском событии, персональной информации

Calendar - Календарь
Календарь, с отмечеными на нём заметками. Основной инструмент для создания,
редактирования и удаления заметок