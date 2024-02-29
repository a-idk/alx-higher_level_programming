/*
 * Script that:
 *	adds
 *	removes
 * 	clears LI elements from a list when the user clicks
 */

$('document').ready(function () {
  // clicking "add_item"
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // clicking the "remove_item
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  // clicking the "clear_list"
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
