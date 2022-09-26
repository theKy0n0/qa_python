from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Как жить если все плохо")
        collector.add_new_book("Мой кот не хочет меня убить")
        assert len(collector.get_books_rating()) == 2

    def test__init__books_rating_type_is_dict(self):
        collector = BooksCollector()
        assert type(collector.books_rating) == dict

    def test__init__books_favorites_type_is_list(self):
        collector = BooksCollector()
        assert type(collector.favorites) == list

    def test_add_new_book_book_cannot_be_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Мой кот не хочет меня убить")
        collector.add_new_book("Мой кот не хочет меня убить")
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_book_not_in_collection(self):
        collector = BooksCollector()
        collector.add_new_book("Мой кот меня любит")
        collector.set_book_rating("У меня нет собаки", 3)
        assert collector.get_book_rating("У меня нет собаки") == None

    def test_set_book_rating_rating_not_over_than_1(self):
        collector = BooksCollector()
        collector.add_new_book("Мой кот меня обожает")
        collector.set_book_rating("Мой кот меня обожает", 0)
        assert collector.get_book_rating("Мой кот меня обожает") == 1

    def test_set_book_rating_rating_more_than_10(self):
        collector = BooksCollector()
        collector.add_new_book("Моя собака умеет ходить в унитаз")
        collector.set_book_rating("Моя собака умеет ходить в унитаз", 11)
        assert collector.get_book_rating("Моя собака умеет ходить в унитаз") == 1

    def test_get_book_rating_book_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book("Мой котик самый лучший")
        assert collector.get_book_rating("Мой котик самый самый лучший") is None

    def test_add_book_in_favorites_book_not_in_list(self):
        collector = BooksCollector()
        assert collector.add_book_in_favorites("Тестирование это не сложно говорили они") == None

    def test_add_book_in_favorites_adding_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Сложно быть мной")
        collector.add_book_in_favorites("Сложно быть мной")
        assert "Сложно быть мной" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book("Новая книга для удаления")
        collector.add_book_in_favorites("Новая книга для удаления")
        collector.delete_book_from_favorites("Новая книга для удаления")
        assert len(collector.get_list_of_favorites_books()) == 0