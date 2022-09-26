# qa_python

1. Тест test__init__books_rating_type_is_dict проверяет, что тип данных у переменной books_rating - словарь
2. Тест test__init__books_favorites_type_is_list проверяет, что тип данных у переменной favorites - список
3. Тест test_add_new_book_book_cannot_be_added_twice проверяет, что книга не добавляется дважды
4. Тест test_set_book_rating_book_not_in_collection проверяет, что книге нельзя добавить рейтинг если ее нет в списке
5. Тест test_set_book_rating_rating_not_over_than_1 проверят, что нельзя добавить рейтинг книге меньше 1
6. Тест test_set_book_rating_rating_more_than_10 проверяет, что нельзя добавить рейтинг больше 10
7. Тест test_get_book_rating_book_not_in_list проверяет, что у книги, которой нету в списке, нет рейтинга
8. Тест test_add_book_in_favorites_book_not_in_list проверяет, что нельзя добавить книгу, которой нет в словаре
9. Тест test_add_book_in_favorites_adding_new_book проверяет, что можно добавить новую книгу в избранное
10. Тест test_delete_book_from_favorites_delete_book проверяет, что добавленная книга удаляется из избранного

