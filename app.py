from flask import Flask, request, render_template, jsonify
import pymysql
import re

app = Flask(__name__)
# MariaDB connection details
db_config = {
    'host': '152.89.239.166',
    'user': 'DA_NeededCodes',
    'password': 'DA_NeededCodes_2024-25',
    'database': 'DA_Needed_Codes',
    'port': 12345
}

def convert_to_sql_like_pattern(search_term):
    search_term = search_term.strip()  # Entferne unnötige Leerzeichen
    if len(search_term) < 2:
        return None  # Wenn die Eingabe zu kurz ist, kann kein gültiges Muster erstellt werden

    first_letter = search_term[0]  # Der erste Buchstabe muss am Anfang stehen
    second_letter = search_term[1]  # Der zweite Buchstabe kann irgendwo vorkommen

    # Muster: Der erste Buchstabe am Anfang, und der zweite irgendwo im Wort
    like_pattern = f"{first_letter}%{second_letter}%"
    return like_pattern


def get_matching_codes(search_term):
    # Verbindung zur MariaDB herstellen
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
            like_pattern = convert_to_sql_like_pattern(search_term)
            if like_pattern is None:
                return []  # Keine Übereinstimmungen, wenn das Muster ungültig ist

            # Verwende LIKE für die Suche nach dem genauen Muster
            query = "SELECT code FROM codes_table WHERE code LIKE %s"
            cursor.execute(query, (like_pattern,))
            result = cursor.fetchall()
            return [row[1] for row in result]
    finally:
        connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    if search_term:
        matching_codes = get_matching_codes(search_term)
        return jsonify(matching_codes)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
