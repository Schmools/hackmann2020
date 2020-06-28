import random
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_question(conn, question):
    """
    Create a new question
    :param conn:
    :param question:
    :return:
    """

    sql = ''' INSERT INTO questions(id,text,total,no,yes)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, question)
    return cur.lastrowid

def count_all_questions(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions")

    rows = cur.fetchall()
    count = 0

    for row in rows:
        count = count + 1

    return count
def print_all_rows(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_question_by_id(conn, id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions WHERE id=?", (id,))

    rows = cur.fetchall()

    #show_questions = []
    for row in rows:
        #show_questions = show_questions + row
        print(row)

def update_question(conn, question):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE questions
              SET total = ? ,
                  yes = ? ,
                  no = ?

            WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def get_yes(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions WHERE id=?", (id,))

    rows = cur.fetchall()
    for row in rows:
        return row[3]

def get_no(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions WHERE id=?", (id,))

    rows = cur.fetchall()
    for row in rows:
        return row[4]

def get_total(conn, id):
    return get_yes(conn, id) + get_no(conn, id);

def vote_yes(conn, id):
    update_question(conn, (get_total(conn, id)+1, get_yes(conn, id) + 1, get_no(conn, id), id))

def vote_no(conn, id):
    update_question(conn, (get_total(conn, id)+1, get_yes(conn, id), get_no(conn, id) + 1, id))

def submit_question(conn, text):
    create_question(count_all_questions(conn), text, 0, 0, 0)
     
def main():
    sql_create_questions_table = """ CREATE TABLE IF NOT EXISTS questions (
                                        id integer PRIMARY KEY,
                                        text text NOT NULL,
                                        total text,
                                        yes text,
                                        no text
                                    ); """

    sql_create_comments_table = """CREATE TABLE IF NOT EXISTS comments (
                                    id integer PRIMARY KEY,
                                    text text NOT NULL
                                );"""

    database = r"C:\sqlite\db\pythonsqlite_test4.db"
    conn = create_connection(database)
    with conn:
         # create projects table
        create_table(conn, sql_create_questions_table)

        # create tasks table
        create_table(conn, sql_create_comments_table)

        question_1 = (1, 'Is Hawaiian pizza good?', 0, 0, 0)
        create_question(conn, question_1)

        question_2 = (2, 'Is a hotdog a sandwich?', 0, 0, 0)
        create_question(conn, question_2)

        question_3 = (3, 'Is cereal a soup?', 0, 0, 0)
        create_question(conn, question_3)

        #ßquestion_

        #this part still doesnt work like it should
        #update_question(conn, (3, 2, 1, 1))

        print("1. Get a question:")
        select_question_by_id(conn, 1)

        print("2. Vote yes on question")
        vote_yes(conn, 1)
        select_question_by_id(conn, 1)

        print("3. Vote no on a question")
        vote_no(conn, 1)
        select_question_by_id(conn, 1)

        print("4. Add a question")
        submit_question(conn, "Is DC better than Marvel?")

        print("5. Get all questions")
        print_all_rows(conn)

        #count function means I know the range for the random ints


#if __name__ == '__main__':
main()
