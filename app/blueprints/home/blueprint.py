from flask import Blueprint, render_template, request
import psycopg2

home = Blueprint('home', __name__)


WRONG_PICTURES = []


@home.route('/',  methods=['POST', 'GET'])
def route_name():
    if request.method == 'GET':
        return render_template('home.html', feedback=False)
    else:
        text = request.form['text']
        WRONG_PICTURES.append(text)
        print(WRONG_PICTURES)
        # save_into_db(text)
        return render_template('home.html', feedback=True)


def create_pictures_table():
    conn = psycopg2.connect(
        user="felix", database="tiki", password="felixpostgre")
    conn.autocommit = True
    cursor = conn.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS pictures(
            name VARCHAR(255)
            );
    """
    try:
        cursor.execute(query)
    except Exception as err:
        print(f'ERROR: {err}')
    cursor.close()


def save_into_db(name_of_picture):
    conn = psycopg2.connect(
        user="felix", database="tiki", password="felixpostgre")
    conn.autocommit = True
    cursor = conn.cursor()
    query = f"""INSERT INTO pictures (name) 
            VALUES (%s);"""
    val = (name_of_picture)
    print(
        f'name: {name_of_picture}')
    try:
        cursor.execute(query, val)
    except Exception as err:
        print(f'ERROR: {err}')
    cursor.close()


create_pictures_table()
