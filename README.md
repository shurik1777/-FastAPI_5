## Так как задача стоит использовать запросы из командной строки

### То для реализации этого задания можно использовать запросы из power shell

- Добавления задачи: 
```
$headers = @{
    "accept" = "application/json"
    "Content-Type" = "application/json"
}

$body = @{
    id = 3
    title = "Task"
    description = "This is task."
    status = "New change"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:8000/tasks" -Method POST -Headers $headers -Body $body
```
- Корректировку задачи(где id - точное id задачи, а в переменной $body - новые данные переданные для объекта json): 
```
$body = @{
    id = 0
    title = "New task"
    description = "New description"
    status = "Changed"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:8000/tasks/id" -Method PUT -Headers $headers -Body $body
```
- Удаление задачи(где id - точное id задачи которое нужно удалить):
```
$headers = @{
    "accept" = "application/json"
    "Content-Type" = "application/json"
}

Invoke-WebRequest -Uri "http://127.0.0.1:8000/tasks/id" -Method DELETE -Headers $headers
```