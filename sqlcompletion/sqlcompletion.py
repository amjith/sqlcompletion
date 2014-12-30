from __future__ import print_function
def suggest_type(sql, cursor_pos=None):
    if cursor_pos is None:
        sql_before_cursor = sql
    else:
        sql_before_cursor = sql[:cursor_pos]

    print(sql_before_cursor)
