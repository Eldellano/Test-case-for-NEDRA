## Тестовое задание для NEDRA digital

>1. Сервис-калькулятор 
С помощью фреймворка FastAPI реализовать сервис, вычисляющий результат арифметического выражения  и предоставляющий возможность просмотреть история запросов. 

___
Задание выполнено с использованием языка Python 3.8 и фреймворка FastAPI 0.74
___
Запуск программы из командной строки - 
`uvicorn main:app`
___
Калькулятор имеет 2 эндпоинта:
* /calc/{expression}
    * expression - выражение для вычисления, например /calc/5 * 7
* /history - может принимать необязательные параметры `limit` и `status`
  * /history?limit=5 вернет 5 последних запросов. Ограничение возможно в диапазоне от 1 до 30 записей. 
  * /history?status=success вернет удачные результаты вычисления
  * /history?status=fail вернет запросы с ошибкой
  Параметры запроса можно комбинировать вместе, например `/history?status=fail&limit=15`
---
Мысли по реализации калькулятора отражены в файле INFO.txt, внутри каталога с кодом.
___