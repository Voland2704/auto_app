# auto_app
Этот проект представляет собой веб-приложение, созданное с использованием фреймворка Flask для языка программирования Python. В приложении реализовано RESTful API, предоставляющее базовый функционал для управления списком предметов.:

GET /api/items: Возвращает список всех предметов в формате JSON.

GET /api/items/int:item_id: Возвращает информацию о предмете с указанным идентификатором в формате JSON.

POST /api/items: Создает новый предмет на основе данных, предоставленных в теле запроса в формате JSON.

PUT /api/items/int:item_id: Обновляет информацию о предмете с указанным идентификатором на основе данных, предоставленных в теле запроса в формате JSON.

DELETE /api/items/int:item_id: Удаляет предмет с указанным идентификатором.
