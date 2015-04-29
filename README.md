# Xblock GradeMe
Button to send request to server to grade user.

## TODO List:
- [ ] Write tests
- [ ] Update the `student_view`
    - [ ] `./xblockgrademe/private/view.html`
        - Add content to `<div class="xblockgrademe_block"></div>` element
    - [ ] `./xblockgrademe/private/view.js`
        - Add logic to `XblockGrademeView` function
    - [ ] `./xblockgrademe/private/view.less`
        - Add styles to `.xblockgrademe_block { }` block
    - [ ] `./xblockgrademe/xblockgrademe.py`
        - Add back-end logic to `student_view` method
- [ ] Update the `studio_view`
    - [ ] `./xblockgrademe/private/edit.html`
        - Add `<LI>` entries to `<ul class="list-input settings-list">` for each new field
    - [ ] `./xblockgrademe/private/edit.js`
        - Add entry for each field to `XblockGrademeEdit`
    - [ ] `./xblockgrademe/private/edit.less`
        - Add styles to `.xblockgrademe_edit { }` block (if needed)
    - [ ] `./xblockgrademe/xblockgrademe.py`
        - Add entry for each field to `studio_view_save`
- [ ] Update package metadata
    - [ ] `./package.json`
        - https://www.npmjs.org/doc/files/package.json.html
    - [ ] `./setup.py`
        - https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
- [ ] Update `./Gruntfile.js`
    - http://gruntjs.com/getting-started
- [ ] Update `./README.markdown`
- [ ] Write documentation
- [ ] Publish on PyPi
