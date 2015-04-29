function XblockGrademeView(runtime, element) {
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);

    var failure_message = 'We are sorry; users who have not created accounts and registered ' +
                          'for the course may not receive a Statement of Accomplishment.';
    
    var success_message = 'Your grading request has been received. If you have passed, your Statement of ' +
                          'Accomplishment should be available on your <a href="/dashboard">account dashboard</a> ' +
                          'page within the next 20 minutes.';

    //TODO: switch this to use the User Service
    var scraped_username = $('li.primary a.user-link').text();

    if (scraped_username) {
        $('.xblockgrademe_block .user_verify_button').addEventListener('click', function (event) {
            (function (event) {
                $.ajax({
                    type: 'POST',
                    url: '/request_certificate',
                    data: {'course_id': $$course_id}, //TODO: switch this to the Course Service when available
                    success: function (data) {
                        $('.xblockgrademe_block .verify-button-message-text').html(success_message);
                    }
                });
            }).call($('.xblockgrademe_block .user_verify_button'), event);
        });
    } else {
        $('.xblockgrademe_block .verify-button-message-text').html(failure_message).addClass('error');
        $('.xblockgrademe_block .user_verify_button').remove();
    }
}
