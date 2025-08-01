# qa_python
# добавили в словарь две книги
test_add_new_book_add_two_books 
# невозможно добавить одну книгу дважды
test_add_new_book_not_add_new_book_two_times 
# добавляем книгу с названием минимальной длинны
test_add_new_book_add_new_book_valid_len_name[x]
# добавляем книгу с названием максимально допустимой длинны
test_add_new_book_add_new_book_valid_len_name[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] 
# добавляем книгу с названием недопустимой длинны(менее 1 символа)
test_add_new_book_add_new_book_invalid_len_name[] 
# добавляем книгу с названием недопустимой длинны(41 символ)
test_add_new_book_add_new_book_invalid_len_name[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] 
# проверяем установку валидного жанра для существующей книги
test_set_book_genre_add_valid_genre_to_existing_book 
# проверяем невозможность установки невалидного жанра для существующей книги
test_set_book_genre_add_invalid_genre_to_existing_book 
# проверяем жанр книги по имени книги
test_get_book_genre_by_book_name 
# проверяем получение книг по жанру
test_get_books_with_specific_genre_got_book_list_has_specific_genre 
# проверяем получение текущего словаря (используя 3 книги)
test_get_books_genre_get_three_books 
# проверяет что книги для детей не состоят в списке, который содержит жанры с возрастным рейтингом
test_get_books_for_children_not_in_genre_age_rating_list 
# проверяет что нельзя добавить книгу в избранное , которой нет в списке
test_add_book_in_favorites_imposible_add_not_in_books_genre 
# проверяет что повторно добавить книгу в избранное нельзя
test_add_book_in_favorites_imposible_add_twice 
# попытка удаления из избранного книги, которой нет в избранном
test_delete_book_from_favorites_not_in_favorites_books 
# проверка на возврат списка, когда нет избранных книг
test_get_list_of_favorites_books_empty_favorites_list 
