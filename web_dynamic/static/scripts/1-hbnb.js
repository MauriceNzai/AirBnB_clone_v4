$(document).ready(function () {
  $('input[type=checkbox]').on('click', function () {
    const amenList = [];
    $('input:checked').each(function () {
      amenList.push($(this).attr('data-name'));
    });
    $('.amenities h4').text(amenList.join(', '));
    if (amenList.length === 0) {
      $('.amenities h4').html('&nbsp;');
    }
  });
});
