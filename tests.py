import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    # 1 проверяум, что книга добавляется
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Братья Карамазовы')

        assert 'Братья Карамазовы' in collector.get_books_genre()

    # 2 проверяем, что не добавляются пустые названия и назания длиннее 40 символов
    @pytest.mark.parametrize('name', ['', 'А'*41])
    def test_add_new_book_invalid_length_not_add(self, name, collector):
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    # 3 проверяем, что у добавленной книги нет жанра
    def test_add_new_book_without_genre(self, collector):
        collector.add_new_book('Братья Карамазовы')
        
        assert collector.get_book_genre('Братья Карамазовы') == ''

    # 4 проверяем возможность установить жанр из списка
    def test_set_book_genre_add_genre_to_book(self, collector):
        collector.add_new_book('Братья Карамазовы')
        collector.set_book_genre('Братья Карамазовы', 'Детективы')

        assert collector.get_book_genre('Братья Карамазовы') == 'Детективы'

    # 5 проверяем, что невозможно установить жанр не из списка
    def test_set_book_genre_add_nonexistent_genre_to_book(self, collector):
        collector.add_new_book('Братья Карамазовы')
        collector.set_book_genre('Братья Карамазовы', 'Мелодрама')
    
        assert collector.get_book_genre('Братья Карамазовы') == ''

    # 6 проверяем, что невозможно добавить жанр к недобавленной книге 
    def test_set_book_genre_book_not_in_collector(self, collector):
        collector.set_book_genre('Неизвестная книга', 'Детективы')

        assert collector.get_book_genre('Неизвестная книга') is None

    # 7 проверяем получение книг по жанру 'Детективы'
    def test_get_books_with_specific_genre_detectives(self, collector):
        collector.add_new_book('Братья Карамазовы')
        collector.add_new_book('Дядюшкин сон')
        collector.set_book_genre('Братья Карамазовы', 'Детективы')
        collector.set_book_genre('Дядюшкин сон', 'Комедии')

        assert collector.get_books_with_specific_genre('Детективы') == ['Братья Карамазовы']

    # 8 проверяем получение книг по жанру 'Комедии'
    def test_get_books_with_specific_genre_comedies(self, collector):
        collector.add_new_book('Братья Карамазовы')
        collector.add_new_book('Дядюшкин сон')
        collector.set_book_genre('Братья Карамазовы', 'Детективы')
        collector.set_book_genre('Дядюшкин сон', 'Комедии')

        assert collector.get_books_with_specific_genre('Комедии') == ['Дядюшкин сон']

    # 9 проверяем, что книги с возрастным рейтингом не попадают в список для детей
    def test_get_books_for_children_excludes_age_rated(self, collector):
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

    # 10 проверяет добавление книги в избранное
    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == ['Властелин колец']

    # 11 проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == []

    # 12 проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Изгоняющий дьявола')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Изгоняющий дьявола')

        assert collector.get_list_of_favorites_books() == ['Властелин колец', 'Изгоняющий дьявола']