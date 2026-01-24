import pytest
from final_task_library import Library, Book, Member
from contextlib import nullcontext as not_raise

@pytest.mark.init_errors
@pytest.mark.parametrize(
    "lib_name, expectations", 
    [
        pytest.param('', pytest.raises(ValueError), id='empty'),
        pytest.param(5555, pytest.raises(TypeError), id='int_instead_str'),
        pytest.param("My Name", not_raise(), id='correct'),
    ]
)
def test_library_init(lib_name, expectations):
    with expectations:
        Library(lib_name) 




@pytest.mark.init_errors
@pytest.mark.parametrize(
    "title, author, isbn, year, expectations", 
    [
        pytest.param('', 'aaa', 'dfdf', 2000, pytest.raises(ValueError), id='empty name'),
        pytest.param('dfdf', 'aaa', 'dfdf', 2000, not_raise(), id='correct'),
        pytest.param(11, 'aaa', 'dfdf', 2000, pytest.raises(TypeError), id='int_instead_str'),
        pytest.param('dfdf', 22, 'dfdf', 2000, pytest.raises(TypeError), id='int_instead_str author'),
        pytest.param('dfdf', 'aaa', '', 2000, pytest.raises(ValueError), id='empty isbn'),
        pytest.param('dfdf', 'aaa', 'dfdf', -1999, pytest.raises(ValueError), id='negative year'),
        pytest.param('dfdf', 'aaa', 'dfdf', 0, pytest.raises(ValueError), id='zero year'),  
        pytest.param('My Name', 'Author', 'ISBN123', 1.5, pytest.raises(TypeError), id='float_instead_int year'),
        pytest.param('My Name', 'Author', 'ISBN123', '2020', pytest.raises(TypeError), id='str_instead_int year'),
    ]
)
def test_book_name_init(title, author, isbn, year, expectations):
    with expectations:
        Book(title, author, isbn, year)


@pytest.mark.init_errors
@pytest.mark.parametrize(
    "member_name, member_id, email, max_books, expectations", 
    [
        pytest.param('', 1, 'a@b.com', 5, pytest.raises(ValueError), id='empty_name'),
        pytest.param('Alice', 'abc', 'a@b.com', 5, pytest.raises(TypeError), id='id_not_int'),
        pytest.param('Bob', -1, 'b@c.com', 5, pytest.raises(ValueError), id='negative_id'),
        pytest.param('Carol', 0, 'c@d.com', 5, pytest.raises(ValueError), id='zero_id'),
        pytest.param(123, 1, 'e@f.com', 5, pytest.raises(TypeError), id='name_not_str'),
        pytest.param('Dave', 2, '', 5, pytest.raises(ValueError), id='empty_email'),
        pytest.param('Eve', 3, 'evemail.com', 5, pytest.raises(ValueError), id='email_no_at'),
        pytest.param('Frank', 4, 12345, 5, pytest.raises(TypeError), id='email_not_str'),
        pytest.param('Grace', 5, 'g@h.com', -1, pytest.raises(ValueError), id='negative_max_books'),
        pytest.param('Heidi', 6, 'h@i.com', 0, pytest.raises(ValueError), id='zero_max_books'),
        pytest.param('Ivan', 7, 'i@j.com', 2.5, pytest.raises(TypeError), id='max_books_not_int'),
        pytest.param('Judy', 8, 'j@k.com', '3', pytest.raises(TypeError), id='max_books_str'),
        pytest.param('Mallory', 9, 'm@n.com', 1, not_raise(), id='correct_min'),
        pytest.param('Oscar', 10, 'o@p.com', 10, not_raise(), id='correct'),
        pytest.param('Peggy', 11, 'peggy@domain.co.uk', 3, not_raise(), id='correct_email_long'),
    ]
)
def test_member_init(member_name, member_id, email, max_books, expectations):
    with expectations:
        Member(member_name, member_id, email, max_books)