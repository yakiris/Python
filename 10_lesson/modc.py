foo = 'foo C'

# if_name_ == '_main_' - Ограничивает выполнение скриптов
# при импорте код не будет выполняться, но выполняется при запуске самого модуля
if __name__ == '__main__':
    print('Я выполняюсь всегда')
    print('Когда меня импортируют')
    print('Ну или почти всегда')