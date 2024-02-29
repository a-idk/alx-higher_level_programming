/*
 * Script that fetche from https://hellosalut.stefanbohacek.dev/?lang=fr
 * and displays the value of hello from that fetch in the HTML tag DIV#hello
 * The translation of “hello” must be displayed in the HTML tag DIV#hello
 */
const web = 'https://fourtonfish.com/hellosalut/?lang=fr';
$('document').ready(function () {
  $.get(web, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
