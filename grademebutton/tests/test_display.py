#!/usr/bin/env python
"""
Test basic XBlock display function
"""
from __future__ import absolute_import
import unittest

from mock import Mock
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from xblock.field_data import DictFieldData

from grademebutton.xblocks import GradeMeButton


def make_an_xblock(**kwargs):
    """
    Helper method that creates a Free-text Response XBlock
    """
    course_id = SlashSeparatedCourseKey('foo', 'bar', 'baz')
    services = {
        'i18n': Mock(ugettext=lambda string: string),
        'user': Mock(
            get_current_user=lambda: Mock(
                emails=['example@fake.com'],
                opt_attrs={},
            ),
        )
    }
    runtime = Mock(
        course_id=course_id,
        service=lambda _, service: services.get(service),
    )
    scope_ids = Mock()
    field_data = DictFieldData(kwargs)
    xblock = GradeMeButton(runtime, field_data, scope_ids)
    xblock.xmodule_runtime = runtime
    return xblock


class TestRender(unittest.TestCase):
    """
    Test the HTML rendering of the XBlock
    """

    def setUp(self):
        self.xblock = make_an_xblock()

    def test_render(self):
        student_view = self.xblock.student_view()
        html = student_view.content
        self.assertIsNotNone(html)
        self.assertNotEqual('', html)
        self.assertIn('grademebutton_block', html)
