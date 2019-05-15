Grade Me Button XBlock
==================
Allow users to self-request a PDF certificate in self-paced courses.

|badge-travis|
|badge-coveralls|


|image-lms-view-normal|


Installation, system administrator
----------------------------------

To install the XBlock on your platform,
add the following to your `requirements.txt` file:

    xblock-grademe

You'll also need to add this to your `INSTALLED_APPS`:

    grademebutton


Installation, course staff
--------------------------

To install the XBlock in your course,
access your `Advanced Module List`:

    Settings -> Advanced Settings -> Advanced Module List

|image-cms-settings-menu|

and add the following:

    grademebutton

|image-cms-advanced-module-list|


Use, Course Staff
-----------------

To add a Grade Me Button to your course:

- go to a unit in Studio
- select "Image Modal XBlock" from the Advanced Components menu

|image-cms-add|

You can now edit and preview the new component.

|image-cms-view|

Using the Studio editor, you can edit the following fields:

- display name
- survey id
- university
- link text
- message
- parameter name for userid

|image-cms-editor-1|
|image-cms-editor-2|


Use, Participants
-----------------

|image-lms-view-normal|

Students click on a link within the unit and this takes them to the survey.

`View a demo of the CMS`_

`View a demo of the LMS`_


.. |badge-coveralls| image:: https://coveralls.io/repos/github/Stanford-Online/xblock-grademe/badge.svg?branch=master
   :target: https://coveralls.io/github/Stanford-Online/xblock-grademe?branch=master
.. |badge-travis| image:: https://travis-ci.org/Stanford-Online/xblock-grademe.svg?branch=master
   :target: https://travis-ci.org/Stanford-Online/xblock-grademe
.. |image-cms-add| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/cms-add.jpg
   :width: 100%
.. |image-cms-advanced-module-list| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/advanced-module-list.png
   :width: 100%
.. |image-cms-editor-1| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/studio-editor-1.png
   :width: 100%
.. |image-cms-editor-2| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/studio-editor-2.png
   :width: 100%
.. |image-cms-settings-menu| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/settings-menu.png
   :width: 100%
.. |image-cms-view| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/studio-view.png
   :width: 100%
.. |image-lms-view-normal| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/lms-view-normal.png
   :width: 100%
.. |image-lms-view-zoom| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/image-modal/static/images/lms-view-zoom.png
   :width: 100%
