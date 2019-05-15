"""
This is the core logic for the XBlock
"""
from __future__ import absolute_import
from xblock.core import XBlock

from .mixins.scenario import XBlockWorkbenchMixin
from .models import GradeMeButtonModelMixin
from .views import GradeMeButtonViewMixin


@XBlock.needs('i18n')
@XBlock.wants('user')
class GradeMeButton(
        GradeMeButtonModelMixin,
        GradeMeButtonViewMixin,
        XBlockWorkbenchMixin,
        XBlock,
):
    """
    A Grade-Me Button XBlock
    """
