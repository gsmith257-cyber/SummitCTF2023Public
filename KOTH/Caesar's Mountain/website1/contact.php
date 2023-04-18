<!DOCTYPE html>
<html>
  <head>
    <title>Caesar's Mountain Safety Contact Form</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Caesar's Mountain Safety Contact Form</h1>

    <form action="contact.php" method="post">
      <label for="name">Name:</label>
      <input type="text" name="name" id="name">

      <label for="email">Email:</label>
      <input type="email" name="email" id="email">

      <label for="phone">Phone:</label>
      <input type="tel" name="phone" id="phone">

      <label for="message">Message:</label>
      <textarea name="message" id="message" rows="5" cols="50"></textarea>

      <input type="submit" value="Submit">
    </form>
  </body>
</html>
