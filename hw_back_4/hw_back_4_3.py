# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


def view_balance() -> float:
    """
    Выводит баланс счёта
    :return:
    """
    print(f'Ваш баланс {balance:.2f} у.е.')
    return balance


def get_out(current_balance: float, value: float, cnt: int) -> (float, int):
    """
    Вывести на баланс денежные средства
    :param current_balance:
    :param value:
    :param cnt:
    :return:
    """
    roskosh = 0
    if current_balance > 5_000_000:
        roskosh = value * 0.1
    if value % 50 == 0 and value >= 0:
        com = value * 0.015
        if com < 30:
            com = 30
        elif com > 600:
            com = 600
        if current_balance - value - com >= 0:
            cnt = cnt + 1
            return -value - com - roskosh, cnt


def get_in(current_balance: float, value: float, cnt: int) -> (float, int):
    """
    Внести на счёт денежные средства
    :param current_balance:
    :param value:
    :param cnt:
    :return:
    """
    roskosh = 0
    if current_balance > 5_000_000:
        roskosh = value * 0.1
    if value % 50 == 0 and value >= 0:
        cnt = cnt + 1
        return value - roskosh, cnt


def percent(current_balance: float, cnt: int) -> (float, int):
    """
    Для подсчета налога на роскошь
    :param current_balance:
    :param cnt:
    :return:
    """
    if cnt > 3:
        current_balance += current_balance * 0.03
        cnt = 0
    return current_balance, cnt


balance = 6_000_000.0
count = 0
view_balance()
tp = get_out(balance, 900.0, count)
percent(balance, count)
balance += tp[0]
count = tp[1]

view_balance()
tp = get_in(balance, 950.0, count)
percent(balance, count)
balance += tp[0]
count = tp[1]

view_balance()
tp = get_in(balance, 950.0, count)
percent(balance, count)
balance += tp[0]
count = tp[1]

view_balance()
tp = get_in(balance, 0.0, count)
percent(balance, count)
balance += tp[0]
count = tp[1]

view_balance()
tp = get_in(balance, 0.0, count)
percent(balance, count)
balance += tp[0]
count = tp[1]
