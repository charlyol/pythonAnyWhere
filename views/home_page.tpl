<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diamond Generator</title>
</head>
<body>
    <h1>Diamond Generator</h1>
    <p>Enter a letter to generate a diamond:</p>
    <form action="/" method="GET">
        <input type="text" size="1" maxlength="1" name="letter">
        <input type="submit" name="generate" value="Generate">
    </form>
    <hr>
    % if diamond_result:
        <pre>{{ diamond_result }}</pre>
    % endif
</body>
</html>
