import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

# tasks = json.loads(r.text)

def count_task_frequency(tasks):
    CompletedTasksFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try: 
                CompletedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                CompletedTasksFrequencyByUser[entry["userId"]] = 1
    return CompletedTasksFrequencyByUser

def user_with_top_completed_task(CompletedTasksFrequencyByUser):
    userIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(CompletedTasksFrequencyByUser.values()) 
    for userid, numerOfCompletedTasks in CompletedTasksFrequencyByUser.items():
        if (numerOfCompletedTasks == maxAmountOfCompletedTask):
            userIdWithMaxCompletedAmountOfTasks.append(userid)
    return userIdWithMaxCompletedAmountOfTasks

def change_list_into_conj_of_params(mylist, key="id"):
    conjParams = key + "="
    lastIteration = len(mylist)
    i=0
    for item in mylist:
        i += 1
        if i == lastIteration:
            conjParams += str(item)
        else:
            conjParams += str(item) + "&" + key + "="
    return conjParams

def get_name(Top_completed_tasks):
    r = requests.get("https://jsonplaceholder.typicode.com/users/",params=conjParams)
    users = r.json()
    for user in users :
        print("Wręczam ciasteczko za największą ilość rozwiązanych zadań do użytkownika: ", user["name"])

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else: 
    CompletedTasksFrequencyByUser = count_task_frequency(tasks)
    UserWithTopCompletedTasks = user_with_top_completed_task(CompletedTasksFrequencyByUser)
    conjParams = change_list_into_conj_of_params(UserWithTopCompletedTasks)
    get_name(UserWithTopCompletedTasks)