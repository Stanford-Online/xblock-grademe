/* eslint-disable no-unused-vars */
/**
 * Initialize the student view
 * @param {Object} runtime - The XBlock JS Runtime
 * @param {Object} element - The containing DOM element for this instance of the XBlock
 * @returns {undefined} nothing
 */
function GradeMeButtonView(runtime, element) {
    /* eslint-enable no-unused-vars */
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);
    /* eslint-disable camelcase */
    /* eslint-disable no-undef */
    var courseId = window.$$course_id || '';
    /* eslint-enable camelcase */
    /* eslint-enable no-undef */
    var $message = $element.find('.grademebutton_block .verify-button-message-text');

    /**
     * Handle AJAX handler response
     * @returns {undefined} nothing
     */
    function onError() {
        $message
            .text('Please try again.')
            .addClass('error')
            .show();
    }

    /**
     * Handle AJAX handler response
     * @returns {undefined} nothing
     */
    function onSuccess() {
        $message.show();
    }

    $element.find('.grademebutton_block .user_verify_button').on('click', function() {
        $message.hide();
        /* eslint-disable camelcase */
        $.ajax({
            type: 'POST',
            url: '/request_certificate',
            data: {
                course_id: courseId,
            }, // TODO: switch this to the Course Service when available
            error: onError,
            success: onSuccess,
        });
        /* eslint-enable camelcase */
    });
}
