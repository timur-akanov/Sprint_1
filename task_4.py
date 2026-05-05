# Задание 4
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

new_tasks.remove('task_005'); completed_tasks.append('task_005')

if 'task_007' in new_tasks:
    new_tasks.remove('task_007')

next_task = new_tasks[-1] if new_tasks else None
print('next_task =', next_task)
