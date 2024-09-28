# Использование %:
#
# Переменные: количество участников первой команды (team1_num).
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
#
# Переменные: количество участников в обеих командах (team1_num, team2_num).
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
#
# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
# Переменные: время за которое команда 2 решила задачи (team1_time).
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
#
# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
#
# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
#
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
#
# Комментарии к заданию:
# В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
# Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать. Например, для challenge_result:


score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/ tasks_total


print('В команде %(name)s участников: %(team1_num)s!' % {'name' : 'Мастера кода' , 'team1_num' : 5})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num' : 5 , 'team2_num' : 6})

print('Команда {} решила задач: {}!' .format ('Мастера кода' , score_1))

print('Команда {} решила задач: {}!' .format ('Волшебники данных' , score_2))
print('{} решили задачи за {} с!' .format ('Волшебники данных' ,  team2_time))
print('{} решили задачи за {} с!' .format ('Мастера кода' ,  team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')








