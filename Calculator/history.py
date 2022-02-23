history = []
cnt_elem_history = 30


def history_add(request, response, status):
    dictionary = dict()
    dictionary['request'] = request
    dictionary['response'] = response
    dictionary['status'] = status
    history.append(dictionary)
    print(history)
    history_check(history)


# храним в списке не больше чем элементов чем cnt_elem_history
def history_check(lst):
    if len(lst) > cnt_elem_history:
        lst.reverse()
        lst.pop()
        lst.reverse()
        history_check(lst)


def history_return(limit: (int, None), status: (str, None)) -> list:
    lst_for_answer = []
    if status is not None:
        for i in history:
            if i['status'] == status:
                lst_for_answer.append(i)
    else:
        for i in history:
            lst_for_answer.append(i)

    if limit is None:
        limit = cnt_elem_history
        # print(lst_for_answer[0:limit])
        lst_for_answer.reverse()
        return lst_for_answer[0:limit]
    else:
        # print(lst_for_answer[0:int(limit)])
        lst_for_answer.reverse()
        return lst_for_answer[0:int(limit)]
