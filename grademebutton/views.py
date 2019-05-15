"""
Handle view logic for the XBlock
"""
from __future__ import absolute_import
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin


class GradeMeButtonViewMixin(
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
):
    """
    Handle view logic for Image Modal XBlock instances
    """

    loader = ResourceLoader(__name__)
    static_js_init = 'GradeMeButtonView'

    def is_anonymous_user(self):
        """
        Check if current user is anonymous
        """
        user_service = self.runtime.service(self, 'user')
        user = user_service.get_current_user()
        email = user.emails[0]
        if 'xblock-workbench.user_id' in user.opt_attrs:
            return False
        if email.endswith('@example.com'):
            return True
        if email.endswith('.example.com'):
            return True
        return False

    def provide_context(self, context=None):
        """
        Build a context dictionary to render the student view
        """
        context = context or {}
        context.update({
            'display_name': self.display_name,
            'description_text': self.description_text,
            'button_text': self.button_text,
            'is_anonymous_user': self.is_anonymous_user(),
        })
        return context
