    Задача 1

    У нас есть 2 таблицы:
    Users – таблица пользователей и
    Orders – таблица с заказами пользователей.
    Таблицы имеют такую структуру:

    Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
    );
    
    Orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    total_amount REAL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
    );

    Требуется написать один SQL-запрос к базе данных, который вернёт:
    name всех пользователей, которые оформили заказов (Orders)
    на общую сумму (total_amount) более 1000руб.
    Если у вас получилось, то дополните запрос таким образом
    чтобы он помимо name возвращал общую сумму всех заказов пользователя.


----------------------------------------------------------------
    Задача 2

    На сервере Flask реализована вот такая обработка маршрута:
    @app.route('/api/people', methods=['GET'])
    def hi_people():
        name = request.args.get('name')
        age = request.args.get('age')
        return {"message": f"Привет, {name}, тебе {age} лет."}
    
    Напишите url, перейдя по которому мы передадим на сервер следующую информацию:
    Имя – «Олег», возраст – «33».
    Сервер использует 3000 порт.

----------------------------------------------------------------
    
    Задача 3
    Напишите код, который присвоит переменной “result” только чётные числа из массива “array”.
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    result = # ваш код
    print(result)
    Ожидаемый вывод:
    [2, 4, 6, 8]