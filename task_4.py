# Задание 4
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.insert(0, new_tasks.pop(4))
print(completed_tasks)
new_tasks.remove('task_007')
new_tasks.reverse()
print(new_tasks)