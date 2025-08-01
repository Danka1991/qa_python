from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_not_add_new_book_two_times(self): # добавляем одну книгу дважды
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name", ["x", "x" * 40])
    def test_add_new_book_add_new_book_valid_len_name(self,name): # добавляем книгу с названием валидной длинны
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name", ["", "x" * 41])
    def test_add_new_book_add_new_book_invalid_len_name(self,name): # добавляем книгу с названием невалидной длинны
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_valid_genre_to_existing_book(self): # Проверяем установку валидного жанра для существующей книги
        collector = BooksCollector()
        collector.add_new_book("Смерть на Ниле")
        collector.set_book_genre("Смерть на Ниле", "Детективы")
        assert collector.get_book_genre("Смерть на Ниле") == "Детективы"

    def test_set_book_genre_add_invalid_genre_to_existing_book(self): # Проверяем невозможность установки невалидного жанра для существующей книги
        collector = BooksCollector()
        collector.add_new_book("Унесённые ветром")
        collector.set_book_genre("Унесённые ветром", "Роман")
        assert collector.get_book_genre("Унесённые ветром") == ""

    def test_get_book_genre_by_book_name(self): # проверяем жанр книги по имени книги
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    def test_get_books_with_specific_genre_got_book_list_has_specific_genre(self): # проверяем получение книг по жанру
        collector = BooksCollector()
        collector.add_new_book("Эркюль Пуаро") 
        collector.add_new_book("Хребты безумия") 
        collector.set_book_genre("Эркюль Пуаро", "Детективы")
        collector.set_book_genre("Хребты безумия", "Ужасы")
        assert collector.get_books_with_specific_genre("Детективы") == ["Эркюль Пуаро"]

    def test_get_books_genre_get_three_books(self): # проверяем получение текущего словаря
        collector = BooksCollector() 
        collector.add_new_book('Властелин колец')
        collector.add_new_book("Дюна")
        collector.add_new_book("Хребты безумия")
        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_not_in_genre_age_rating_list(self): # проверяет что книги для детей не состоят в списке, который содержит жанры с возрастным рейтингом.
        collector = BooksCollector()
        collector.add_new_book('Дневник героя')
        collector.add_new_book('Буратино')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Смерть на Ниле')
        collector.set_book_genre('Дневник героя', 'Фантастика')
        collector.set_book_genre('Буратино', 'Мультфильмы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Смерть на Ниле', 'Детективы')
        books_for_kids = collector.get_books_for_children()
        all_books = collector.get_books_genre()
        for book in books_for_kids:
            assert all_books[book] not in collector.genre_age_rating

    def test_add_book_in_favorites_imposible_add_not_in_books_genre(self): # проверяет что нельзя добавить книгу в избранное , которой нет в списке
        collector = BooksCollector()
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_imposible_add_twice(self): # проверяет что повторно добавить книгу в избранное нельзя
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_not_in_favorites_books(self): # попытка удаления из избранного книги, которой нет в избранном
        collector = BooksCollector()
        collector.add_new_book('Дневник героя') 
        collector.delete_book_from_favorites('Дневник героя') 
        assert len(collector.get_list_of_favorites_books()) == 0
 
    def test_get_list_of_favorites_books_empty_favorites_list(self): # проверка на возврат списка, когда нет избранных книг
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []