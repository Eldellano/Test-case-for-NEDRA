## Тестовое задание для NEDRA digital

![https://img.shields.io/badge/Python-3.8-blue](https://img.shields.io/badge/Python-3.8-blue)
![https://img.shields.io/badge/FastAPI-0.74-blue](https://img.shields.io/badge/FastAPI-0.74-blue)

#### Задание 1
>1. Сервис-калькулятор. С помощью фреймворка FastAPI реализовать сервис, вычисляющий 
    результат арифметического выражения и предоставляющий возможность просмотреть историю 
    запросов.

___
Запуск программы из командной строки - 
`uvicorn main:app`
___
Калькулятор имеет 2 эндпоинта:
* /calc/expression
    * expression - выражение для вычисления, например `/calc/5 * 7`
* /history - может принимать необязательные параметры `limit` и `status`
  * /history?limit=5 вернет 5 последних запросов. Ограничение возможно в диапазоне от 1 до 30 записей. 
  * /history?status=success вернет удачные результаты вычисления
  * /history?status=fail вернет запросы с ошибкой.
  
Параметры запроса можно комбинировать вместе, например `/history?status=fail&limit=15`

---
Мысли по реализации калькулятора отражены в файле INFO.txt, внутри каталога Calculator.

___
#### Задание 2
>2. Игра "Крестики-нолики". 
Реализовать программу, играющую в игру Крестики-нолики на поле 3*3.
___

 * Два игрока - player_1 и player_2. 
 * Очередность ходов определяется случайным образом.
 * Компьютер играет сам с собой и выводит в консоль каждый ход.
 * В конце игры выводится результат в виде - Выиграл игрок 1, выиграл игрок 2, ничья.
___
Пример описания хода игрока:
```
Игрок player_1 ставит x на строку "1" столбец "2"
['-', 'x', '-']
['-', '-', '-']
['-', '-', '-']
```

___
