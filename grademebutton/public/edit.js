function GrademebuttonEdit(runtime, element) {
    'use strict';

    var $ = window.$;
    var $element = $(element);
    var buttonSave = $element.find('.save-button');
    var buttonCancel = $element.find('.cancel-button');
    var url = runtime.handlerUrl(element, 'studio_view_save');

    buttonCancel.on('click', function () {
        runtime.notify('cancel', {});
        return false;
    });

    buttonSave.on('click', function () {
        runtime.notify('save', {
            message: 'Saving...',
            state: 'start',
        });
        $.ajax(url, {
            type: 'POST',
            data: JSON.stringify({
                'display_name': $('#grademebutton_display_name').value,
                'description_text': $('#grademebutton_description_text').value,
                'button_text': $('#grademebutton_button_text').value,
            }),
            success: function buttonSaveOnSuccess() {
                runtime.notify('save', {
                    state: 'end',
                });
            },
            error: function buttonSaveOnError() {
                runtime.notify('error', {});
            }
        });
        return false;
    });
}
