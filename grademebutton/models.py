"""
Handle data access logic for the XBlock
"""
from __future__ import absolute_import
from xblock.fields import Scope
from xblock.fields import String


class GradeMeButtonModelMixin(object):
    """
    Handle data access for XBlock instances
    """

    editable_fields = [
        'display_name',
        'description_text',
        'button_text',
    ]

    button_text = String(
        default="Yes, I have completed this course.",
        scope=Scope.settings,
        help="This is the text displayed on the button.",
    )
    description_text = String(
        default=(
            "By clicking the button below, you assert that you have "
            "completed the course in its entirety. Your current score "
            "on the Progress page will be used to determine if you have "
            "earned a Statement of Accomplishment and for what level "
            "you qualify. Do not click the button below until you have "
            "finished the course and are satisfied with your score."
        ),
        scope=Scope.settings,
        help="This is the description of what clicking the button means.",
    )
    display_name = String(
        default='"Grade Me" Button',
        scope=Scope.settings,
        help="The name of the 'Grade Me' button",
    )
