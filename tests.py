import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1 проверяем, что не добавляются пустые названия и назания длиннее 40 символов
    @pytest.mark.parametrize('name', ['', 'А'*41])
    def test_add_new_book_invalid_length_not_add(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    # 2 проверяем, что у добавленной книги нет жанра
    def test_set_book_genre_add_genre_to_book(self):
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.set_book_genre('Братья Карамазовы', 'Детективы')
        
        assert collector.get_book_genre('Братья Карамазовы') == 'Детективы'

    # 3 проверяем возможность установить жанр из списка
    def test_set_book_genre_add_genre_to_book(self):
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.set_book_genre('Братья Карамазовы', 'Детективы')

        assert collector.get_book_genre('Братья Карамазовы') == 'Детективы'

    # 4 проверяем, что невозможно установить жанр не из списка
    def test_set_book_genre_add_nonexistent_genre_to_book(self):
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.set_book_genre('Братья Карамазовы', 'Мелодрама')
    
        assert collector.get_book_genre('Братья Карамазовы') == ''

    # 5 проверяем, что невозможно добавить жанр к недобавленной книге 
    def test_set_book_genre_book_not_in_collector(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Детективы')

        assert collector.get_book_genre('Неизвестная книга') is None

    # 6 проверяем проверяем получение книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.add_new_book('Дядюшкин сон')
        collector.set_book_genre('Братья Карамазовы', 'Детективы')
        collector.set_book_genre('Дядюшкин сон', 'Комедии')

        assert collector.get_books_with_specific_genre('Детективы') == ['Братья Карамазовы']
        assert collector.get_books_with_specific_genre('Комедии') == ['Дядюшкин сон']

    # 7 проверяем, что книги с возрастным рейтингом не попадают в список для детей
    def test_get_books_for_children_excludes_age_rated(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Изгоняющий дьявола')
        collector.add_new_book('Десять негритят')
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Изгоняющий дьявола', 'Ужасы')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        children_books = collector.get_books_for_children()

        assert children_books == ['Властелин колец', 'Незнайка']
        assert 'Изгоняющий дьявола' not in children_books
        assert 'Десять негритят' not in children_books

    # 8 проверяет добавление книги в избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == ['Властелин колец']

    # 9 проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == []

    # 10 проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Изгоняющий дьявола')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Изгоняющий дьявола')

        assert collector.get_list_of_favorites_books() == ['Властелин колец', 'Изгоняющий дьявола']