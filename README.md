# qa_python
список тестов:
1 проверяем, что не добавляются пустые названия и назания длиннее 40 символов - test_set_book_genre_invalid_length_not_add
2 проверяем, что у добавленной книги нет жанра - test_add_new_book_genre_is_empty
3 проверяем возможность установить жанр из списка - test_set_book_genre_add_genre_to_book
4 проверяем, что невозможно установить жанр не из списка - test_set_book_genre_add_genre_to_book
5 проверяем, что невозможно добавить жанр к недобавленной книге - test_set_book_genre_book_not_in_collector
6 проверяем проверяем получение книг по жанру - test_get_books_with_specific_genre
7 проверяем, что книги с возрастным рейтингом не попадают в список для детей - test_get_books_for_children_excludes_age_rated
8 проверяет добавление книги в избранное - test_add_book_in_favorites_success
9 проверяем удаление книги из избранного - test_delete_book_from_favorites
10 проверяем получение списка избранных книг - test_get_list_of_favorites_books