<!DOCTYPE html>
<html>
<head>
    <title>Combined Table</title>
</head>
<body>
    <h2>Combined Table</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Social Media Platform</th>
            <th>Social Media Username</th>
            <th>Event Name</th>
            <th>Event Organizer</th>
            <th>Actions</th>
        </tr>
        % for row in combined_table:
            <tr>
                % for cell in row[:5]:
                    <td>{{cell}}</td>
                % end
                <td>
                    <a href="/edit/{{row[0]}}">Edit</a>
                    <a href="/delete/{{row[0]}}">Delete</a>
                </td>
            </tr>
        % end
    </table>

    <h2>Add Social Media</h2>
    <form action="/add_social_media" method="post">
        <label for="platform">Platform:</label>
        <input type="text" name="platform" required>
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <input type="submit" value="Add Social Media">
    </form>
    
    <h2>Add Event Management</h2>
    <form action="/add_event_management" method="post">
        <label for="event_name">Event Name:</label>
        <input type="text" name="event_name" required>
        <label for="organizer">Organizer:</label>
        <input type="text" name="organizer" required>
        <input type="submit" value="Add Event Management">
    </form>
</body>
</html>
