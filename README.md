# qa_python_sprint_2
список тестов:

1 проверяум, что книга добавляется - test_add_new_book_add_one_book
2 проверяем, что не добавляются пустые названия и назания длиннее 40 символов - test_add_new_book_invalid_length_not_add
3 проверяем, что у добавленной книги нет жанра - test_add_new_book_without_genre
4 проверяем возможность установить жанр из списка - test_set_book_genre_add_genre_to_book
5 проверяем, что невозможно установить жанр не из списка - test_set_book_genre_add_nonexistent_genre_to_book
6 проверяем, что невозможно добавить жанр к недобавленной книге - test_set_book_genre_book_not_in_collector
7 проверяем получение книг по жанру 'Детективы' - test_get_books_with_specific_genre_detectives
8 проверяем получение книг по жанру 'Комедии' - test_get_books_with_specific_genre_comedies
9 проверяем, что книги с возрастным рейтингом не попадают в список для детей - test_get_books_for_children_excludes_age_rated
10 проверяет добавление книги в избранное - test_add_book_in_favorites_success
11 проверяем удаление книги из избранного - test_delete_book_from_favorites
12 проверяем получение списка избранных книг - test_get_list_of_favorites_books