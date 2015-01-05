
$(document).ready(function() {
    $('p.flash_message').fadeIn(600);
    $('p.flash_message').delay(3000).fadeTo(600, 0);
});

$('div.post_listing').hover(function() {
    $(this).find('img.post_image').css('width', '100%');
    $(this).find('div.post_list_left').css('width', '300px');
    $(this).find('div.post_list_right').css('width', '200px');
}, function() {
    $(this).find('img.post_image').css('width', '100%');
    $(this).find('div.post_list_left').css('width', '200px');
    $(this).find('div.post_list_right').css('width', '300px');
});