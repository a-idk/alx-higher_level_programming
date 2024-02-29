/*
 * Script that updates the text of the <header> element to New Header!!!
 * when the user clicks on the tag DIV#update_header
 */
$('DIV#update_header').click(function () {
  $('HEADER').text('New Header!!!');
});
