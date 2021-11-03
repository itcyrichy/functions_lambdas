# 1
def victorina():
    right_answers=0
    wrong_answers=0
    right_answers, wrong_answers = q1(right_answers, wrong_answers)
    right_answers, wrong_answers = q2(right_answers, wrong_answers)
    right_answers, wrong_answers = q3(right_answers, wrong_answers)
    right_answers, wrong_answers = q4(right_answers, wrong_answers)
    right_answers, wrong_answers = q5(right_answers, wrong_answers)

    print(f'Правильные ответы: {right_answers}, неправильные ответы: {wrong_answers}')
    print(f'% првильных ответов: {right_answers/5*100}%')

def q1(right_answers,wrong_answers):
    a1 = input('Когда вступил в должность Джордж Вашингтон?(формат: 01.01.1900, без кавычек)')
    if a1 == '30.02.1789':
        print('Верно!')
        right_answers += 1
    else:
        print('Тридцатого апреля 1789 года')
        wrong_answers += 1
    return right_answers,wrong_answers

def q2(right_answers,wrong_answers):
    a2 = input('Когда вступил в должность Джон Адамс?(формат: 01.01.1900, без кавычек)')
    if a2 == '04.03.1797':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1797 года')
        wrong_answers += 1
    return right_answers,wrong_answers


def q3(right_answers, wrong_answers):
    a3 = input('Когда вступил в должность Томас Джефферсон?(формат: 01.01.1900, без кавычек)')
    if a3 == '04.03.1801':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1801 года')
        wrong_answers += 1
    return right_answers,wrong_answers

def q4(right_answers, wrong_answers):
    a4 = input('Когда вступил в должность Джеймс Мэдисон?(формат: 01.01.1900, без кавычек)')
    if a4 == '04.03.1809':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1809')
        wrong_answers += 1
    return right_answers,wrong_answers

def q5(right_answers, wrong_answers):
    a5 = input('Когда вступил в должность Джеймс Монро?(формат: 01.01.1900, без кавычек)')
    if a5 == '04.03.1817':
        print('Верно!')
        right_answers += 1
    else:
        print('Четвертого марта 1817 года')
        wrong_answers += 1
    return right_answers, wrong_answers

victorina()

# 2

# 3. написать программу "Личный счет"
# Описание работы программы:
# Пользователь запускает программу у него на счету 0 руб
# Программа предлагает следующие варианты действий (основное меню):
# - пополнить счет (при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет,
# /после того как пользователь вводит сумму она добавляется к счету, снова попадаем в основное меню)
# - совершить покупку (при выборе этого пункта пользователю предлагается ввести сумму покупки,
# /если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню,
# /если денег достаточно предлагаем пользователю ввести название покупки, например (еда), снимаем деньги со счета,
# /сохраняем покупку в историю, выходим в основное меню)
# - история покупок (выводим историю покупок пользователя (название и сумму),возвращаемся в основное меню)
# - выход (завершение цикла, выход из меню)
class User:
    def __init__(self,balance,history):
        self.balance = balance
        self.history = history

def proga(some_user='new'):
    if some_user == 'new':
        user = User(0,{})
        history = {}
    else:
        user = some_user
        history = user.history

    StartPage = True
    while StartPage:
        step1 = input('Запустить программу? Для запуска ответьте "да" (без кавычек, пробелов) ')
        if step1 == 'да':
            StartPage = False
            continue
        else:
            print('Возврат на начальную страницу')
    exit_proga = False
    while not exit_proga:
        action = input(f'Ваш баланс равен {user.balance},выберите действие: пополнить баланс/совершить покупку/выйти/история покупок) ')
        if action == 'выйти':
            exit_proga = True
        elif action == 'пополнить баланс':
            add_sum = input('Введите сумму пополнения баланса: ')
            try:
                user.balance = int(user.balance) + int(add_sum)
            except:
                print('Баланс не был пополнен, в следующий раз введите число')
        elif action == 'совершить покупку':
            try:
                purchase_sum = int(input('Введите сумму покупки: '))
                if user.balance >= purchase_sum:
                    good_name = input('Введите название товара: ')
                    if good_name in history:
                        user.balance -= purchase_sum
                        history[good_name] = purchase_sum + int(history[good_name])
                    else:
                        user.balance -= purchase_sum
                        history[good_name] = purchase_sum
                    user.history = history
                else:
                    print(f'Вашего баланса ({user.balance}) недостаточно. Пополните баланс')
            except:
                print('Введённое значение не является числом, в следующий раз введите целое число')
        elif action == 'история покупок':
            print(history)
    return user


user = proga(some_user='new')
print(user.balance,user.history)