from sqlcompletion import suggest_type


def test_select_suggests_cols_with_table_scope():
    suggestion = suggest_type('SELECT  FROM tabl', len('SELECT '))
    assert suggestion == ('columns-and-functions', ['tabl'])

def test_where_suggests_columns_functions():
    suggestion = suggest_type('SELECT * FROM tabl WHERE ', len('SELECT * FROM tabl WHERE '))
    assert suggestion == ('columns-and-functions', ['tabl'])

def test_lparen_suggests_cols():
    suggestion = suggest_type('SELECT MAX( FROM tbl', len('SELECT MAX('))
    assert suggestion == ('columns', ['tbl'])

def test_select_suggests_cols_and_funcs():
    suggestion = suggest_type('SELECT ', len('SELECT '))
    assert suggestion == ('columns-and-functions', [])

def test_from_suggests_tables():
    suggestion = suggest_type('SELECT * FROM ', len('SELECT * FROM '))
    assert suggestion == ('tables', [])

def test_distinct_suggests_cols():
    suggestion = suggest_type('SELECT DISTINCT ', len('SELECT DISTINCT '))
    assert suggestion == ('columns', [])

def test_col_comma_suggests_cols():
    suggestion = suggest_type('SELECT a, b, FROM tbl', len('SELECT a, b,'))
    assert suggestion == ('columns-and-functions', ['tbl'])

def test_table_comma_suggests_tables():
    suggestion = suggest_type('SELECT a, b FROM tbl1, ', len('SELECT a, b FROM tbl1, '))
    assert suggestion == ('tables', [])

def test_into_suggests_tables():
    suggestion = suggest_type('INSERT INTO ', len('INSERT INTO '))
    assert suggestion == ('tables', [])

def test_insert_into_lparen_suggests_cols():
    suggestion = suggest_type('INSERT INTO abc (', len('INSERT INTO abc ('))
    assert suggestion == ('columns', ['abc'])

def test_insert_into_lparen_partial_text_suggests_cols():
    suggestion = suggest_type('INSERT INTO abc (i', len('INSERT INTO abc (i'))
    assert suggestion == ('columns', ['abc'])

def test_insert_into_lparen_comma_suggests_cols():
    suggestion = suggest_type('INSERT INTO abc (id,', len('INSERT INTO abc (id,'))
    assert suggestion == ('columns', ['abc'])

def test_partially_typed_col_name_suggests_col_names():
    suggestion = suggest_type('SELECT * FROM tabl WHERE col_n', len('SELECT * FROM tabl WHERE col_n'))
    assert suggestion == ('columns-and-functions', ['tabl'])

def test_dot_suggests_cols_of_a_table():
    suggestion = suggest_type('SELECT tabl. FROM tabl', len('SELECT tabl.'))
    assert suggestion == ('columns', ['tabl'])

def test_dot_suggests_cols_of_an_alias():
    suggestion = suggest_type('SELECT t1. FROM tabl1 t1, tabl2 t2', len('SELECT t1.'))
    assert suggestion == ('columns', ['tabl1'])

def test_dot_col_comma_suggests_cols():
    suggestion = suggest_type('SELECT t1.a, t2. FROM tabl1 t1, tabl2 t2', len('SELECT t1.a, t2.'))
    assert suggestion == ('columns', ['tabl2'])

def test_sub_select_suggests_keyword():
    suggestion = suggest_type('SELECT * FROM (', len('SELECT * FROM ('))
    assert suggestion == ('keywords', [])

def test_sub_select_table_name_completion():
    suggestion = suggest_type('SELECT * FROM (SELECT * FROM ', len('SELECT * FROM (SELECT * FROM '))
    assert suggestion == ('tables', [])

def test_sub_select_col_name_completion():
    suggestion = suggest_type('SELECT * FROM (SELECT  FROM abc', len('SELECT * FROM (SELECT '))
    assert suggestion == ('columns-and-functions', ['abc'])

def test_sub_select_multiple_col_name_completion():
    suggestion = suggest_type('SELECT * FROM (SELECT a, FROM abc', len('SELECT * FROM (SELECT a, '))
    assert suggestion == ('columns-and-functions', ['abc'])

def test_sub_select_dot_col_name_completion():
    suggestion = suggest_type('SELECT * FROM (SELECT t. FROM tabl t', len('SELECT * FROM (SELECT t.'))
    assert suggestion == ('columns', ['tabl'])
