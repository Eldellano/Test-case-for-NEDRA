from typing import Set, Union
from fastapi import FastAPI
from string import digits
from operator import truediv, mul, add, sub
from decimal import *
import history

app = FastAPI()


@app.get('/calc/{exp1}/{exp2}')
def for_div(exp1: str, exp2: str) -> Union[str, Set[Decimal]]:
    exp_full = f'{exp1}/{exp2}'
    return return_num(exp_full)


@app.get('/calc/{expression}')
def return_num(expression: str) -> Union[str, Set[Decimal]]:
    number_1 = None
    number_2 = None
    cnt = 0  # счетчик индексов
    expression_list = []
    for i in expression.replace(' ', ''):
        if cnt == 0 and (i in ('+', '-') or i in digits):
            cnt += 1
        elif i in ('*', '/', '+', '-'):
            number_1 = expression.replace(' ', '')[0: cnt]
            number_2 = expression.replace(' ', '')[cnt + 1:]
            if number_1[-1] == '.':
                number_1 += '0'
            if number_2[-1] == '.':
                number_2 += '0'
            operation = i
            expression_list.append(number_1)
            expression_list.append(operation)
            expression_list.append(number_2)
            break
        else:
            cnt += 1
    try:
        if number_2 is None:
            history.history_add(expression, expression, 'success')
            return expression
        elif number_1[0] in ('*', '/') or number_2[0] in ('*', '/', '+', '-'):
            history.history_add(expression, '', 'fail')
            return 'Ошибка'
        elif len(number_1) > 1 and not number_1[-1].isdigit() or len(number_2) > 1 and not number_2[-1].isdigit():
            history.history_add(expression, '', 'fail')
            return 'Ошибка'
    except IndexError:
        history.history_add(expression, '', 'fail')
        return 'Ошибка'

    answer = calc(expression_list)
    history.history_add(expression, str(answer), 'success')
    return {answer}


operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


def calc(lst: list) -> Decimal:
    num_1 = Decimal(lst[0])
    num_2 = Decimal(lst[2])
    num_1 = num_1.quantize(Decimal("1.000"))
    num_2 = num_2.quantize(Decimal("1.000"))
    return operators[lst[1]](num_1, num_2).quantize(Decimal("1.000"))


@app.get('/history')
def hist(limit=None, status=None):
    if limit is not None and (0 >= int(limit) or int(limit) > 30):
        return 'Ошибка'
    if status is not None and (str(status) not in ('fail', 'success')):
        return 'Ошибка'
    return history.history_return(limit, status)
