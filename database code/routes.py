from flask import render_template
from app import app
import random
import sqlite3
from sqlite3 import Error

@app.route('/')
@app.route('/index')
def index():
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

        show_questions = []
        for row in rows:
            show_questions = show_questions + row

    def update_question(conn, task):
        """
        update priority, begin_date, and end date of a task
        :param conn:
        :param task:
        :return: project id
        """
        sql = ''' UPDATE questions
                  SET total = ?,
                      yes = ?,
                      no = ?

                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()

    def main():
        database = r"C:\sqlite\db\pythonsqlite.db"
        conn = create_connection(database)
        with conn:

            question_1 = (1, 'Is a hotdog a sandwich?', 0, 0, 0)
            create_question(conn, question_1)

            print("1. Query task by priority:")
            select_question_by_id(conn, 'random int')

            #this part still doesnt work like it should
            update_question(conn, (1, 2, 0, 1))

            #count function means I know the range for the random ints


    if __name__ == '__main__':
        main()

    #show_questions = [random.choice(questions), random.choice(questions)]
    return render_template('index.html', title='Home', user=user, questions=show_questions)
