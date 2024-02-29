/*
 * Script that fetches and prints how to say “Hello”
 * depending on the language
 */

$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const Translate = $('INPUT#language_code').val();
    const web = 'https://fourtonfish.com/hellosalut/?lang=' + Translate;
    $.get(web, function (data, textStatus) {
      console.log(web, data, textStatus);
      // checking for valid response
      if (data.code !== 'none') {
        $('DIV#hello').text(data.hello);
      } else {
        $('DIV#hello').text('Invalid Language code');
      }
    });
  });
});
