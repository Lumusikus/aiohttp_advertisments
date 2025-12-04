# aiohttp_advertisments
Домашнее задание к лекции «Aiohttp»

## API Endpoints

### POST `/ads` - Создать объявление
**Тело запроса (JSON):**
```
{
  "title": "Продам квартиру",
  "description": "3-комнатная, 100 м²",
  "owner": "Иван Иванов"
}
```
### GET /ads - Получить все объявления

### GET /ads/{id} - Получить объявление по ID
```http://localhost:8080/ads/1```
```
{
  "title": "Обновлённый заголовок",
  "description": "Новое описание",
  "owner": "Новый владелец"
}
```

### DELETE /ads/{id} - Удалить объявление
