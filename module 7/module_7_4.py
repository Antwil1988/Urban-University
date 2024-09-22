def total_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return "Победа команды Мастера кода!"
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return "Победа команды Волшебники Данных!"
    return "Ничья!"


score_1 = 5
score_2 = 6

tasks_total = score_1 + score_2
team1_time = 5
team2_time = 4
time_avg = (team1_time + team2_time) / 2

team1_num = 5
team2_num = 6

print(tasks_total)
print(time_avg)
result = total_result(score_1, score_2, team1_time, team2_time)

# Использование %:

print("В команде Мастера кода участников: %s !" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

# Использование format():

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} c!".format(team1_time))

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")