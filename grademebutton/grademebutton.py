"""
This is the core logic for the Xblock GradeMe
"""
import os

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment
import cgi


class Grademebutton(XBlock):
    """
    Button to send request to server to grade user.
    """

    @staticmethod
    def workbench_scenarios():
        """
        Gather scenarios to be displayed in the workbench
        """
        return [
            ('Xblock GradeMe',
             """<sequence_demo>
                    <grademebutton />
                </sequence_demo>
             """),
        ]

    display_name = String(
        default='"Grade Me" Button',
        scope=Scope.settings,
        help="The name of the 'Grade Me' button",
    )

    description_text = String(
        default=("By clicking the button below, you assert that you have completed the course in its entirety. "
                "Your current score on the Progress page will be used to determine if you have earned a Statement of "
                "Accomplishment and for what level you qualify. Do not click the button below until you have "
                "finished the course and are satisfied with your score."
                ),
        scope=Scope.settings,
        help="This is the description of what clicking the button means.",
    )

    button_text = String(
        default="Yes, I have completed this course.",
        scope=Scope.settings,
        help="This is the text displayed on the button.",
    )

    # Decorate the view in order to support multiple devices e.g. mobile
    # See: https://openedx.atlassian.net/wiki/display/MA/Course+Blocks+API
    # section 'View @supports(multi_device) decorator'
    @XBlock.supports('multi_device')
    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """
        fragment = self.build_fragment(
            path_html='view.html',
            paths_css=[
                'view.less.min.css',
            ],
            paths_js=[
                'view.js.min.js',
            ],
            fragment_js='GrademebuttonView',
            context={
                'display_name': cgi.escape(self.display_name, quote=True),
                'description_text': cgi.escape(self.description_text),
                'button_text': cgi.escape(self.button_text, quote=True),
            },
        )
        return fragment

    def studio_view(self, context=None):
        """
        Build the fragment for the edit/studio view

        Implementation is optional.
        """
        fragment = self.build_fragment(
            path_html='edit.html',
            paths_css=[
                'edit.less.min.css',
            ],
            paths_js=[
                'edit.js.min.js',
            ],
            fragment_js='GrademebuttonEdit',
            context={
                'display_name': cgi.escape(self.display_name, quote=True),
                'description_text': cgi.escape(self.description_text),
                'button_text': cgi.escape(self.button_text, quote=True),
            },
        )
        return fragment

    @XBlock.json_handler
    def studio_view_save(self, data, suffix=''):
        """
        Save XBlock fields

        Returns: the new field values
        """

        self.display_name = data['display_name']
        self.description_text = data['description_text']
        self.button_text = data['button_text']

        return {
            'display_name': self.display_name,
            'description_text': self.description_text,
            'button_text': self.button_text,
        }

    def get_resource_string(self, path):
        """
        Retrieve string contents for the file path
        """
        path = os.path.join('public', path)
        resource_string = pkg_resources.resource_string(__name__, path)
        return resource_string.decode('utf8')

    def get_resource_url(self, path):
        """
        Retrieve a public URL for the file path
        """
        path = os.path.join('public', path)
        resource_url = self.runtime.local_resource_url(self, path)
        return resource_url

    def build_fragment(self,
        path_html='',
        paths_css=[],
        paths_js=[],
        urls_css=[],
        urls_js=[],
        fragment_js=None,
        context=None,
    ):
        """
        Assemble the HTML, JS, and CSS for an XBlock fragment
        """
        html_source = self.get_resource_string(path_html)
        html_source = html_source.format(
            self=self,
            **context
        )
        fragment = Fragment(html_source)
        for url in urls_css:
            fragment.add_css_url(url)
        for path in paths_css:
            url = self.get_resource_url(path)
            fragment.add_css_url(url)
        for url in urls_js:
            fragment.add_javascript_url(url)
        for path in paths_js:
            url = self.get_resource_url(path)
            fragment.add_javascript_url(url)
        if fragment_js:
            fragment.initialize_js(fragment_js)
        return fragment
