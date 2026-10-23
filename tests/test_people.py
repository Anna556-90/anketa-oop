import pytest
from people import Person, Student, AnketaError

def test_person_valid():
    # Проверяем, что правильные данные создают объект
    p = Person("иванов иван", "ivanov@mail.ru", "+79211112233")
    assert p.fio == "Иванов Иван"
    assert p.phone == "79211112233"

def test_person_bad_mail():
    # Проверяем, что плохая почта вызывает наше исключение
    with pytest.raises(AnketaError):
        Person("Иванов Иван", "badmail", "+79211112233")

def test_student_empty_group():
    # Проверяем пустую группу
    with pytest.raises(AnketaError):
        Student("Иванов Иван", "ivanov@mail.ru", "+79211112233", "")