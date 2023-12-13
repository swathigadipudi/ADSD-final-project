<!DOCTYPE html>
<html>
<head>
    <title>Edit Entry</title>
</head>
<body>
    <h2>Edit Entry</h2>
    <form action="/update/{{entry_id}}" method="post">
        <!-- Include input fields with existing values for editing -->
        <!-- Replace the following with your actual fields -->
        <label for="new_value">New Value:</label>
        <input type="text" name="new_value" required>
        <input type="submit" value="Update">
    </form>
    <a href="/">Cancel</a>
</body>
</html>
