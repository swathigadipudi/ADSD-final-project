from bottle import Bottle, template, request, redirect
from database import init_db, add_social_media, add_event_management, get_combined_table

app = Bottle()

# Initialize the database
init_db()

@app.route('/')
def index():
    combined_table = get_combined_table()
    return template('index', combined_table=combined_table)

@app.route('/add_social_media', method='POST')
def add_social_media_route():
    platform = request.forms.get('platform')
    username = request.forms.get('username')

    add_social_media(platform, username)

    return redirect('/')

@app.route('/add_event_management', method='POST')
def add_event_management_route():
    event_name = request.forms.get('event_name')
    organizer = request.forms.get('organizer')

    add_event_management(event_name, organizer)

    return redirect('/')

@app.route('/edit/<entry_id>')
def edit(entry_id):
    # You can implement edit logic here
    return template('edit', entry_id=entry_id)

@app.route('/delete/<entry_id>')
def delete(entry_id):
    # You can implement delete logic here
    return redirect('/')

@app.route('/update/<entry_id>', method='POST')
def update(entry_id):
    # Implement update logic here
    new_value = request.forms.get('new_value')

    # Update the database with the new value for the specified entry_id
    # Example: cursor.execute("UPDATE my_table SET my_column = ? WHERE id = ?", (new_value, entry_id))

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
