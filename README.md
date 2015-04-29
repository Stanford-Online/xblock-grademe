# Xblock GradeMe
Button to send request to server to grade user.

## TODO List:
- [ ] Write tests
- [ ] Update the `student_view`
    - [ ] `./grademebutton/private/view.html`
        - Add content to `<div class="grademebutton_block"></div>` element
    - [ ] `./grademebutton/private/view.js`
        - Add logic to `GrademebuttonView` function
    - [ ] `./grademebutton/private/view.less`
        - Add styles to `.grademebutton_block { }` block
    - [ ] `./grademebutton/grademebutton.py`
        - Add back-end logic to `student_view` method
- [ ] Update the `studio_view`
    - [ ] `./grademebutton/private/edit.html`
        - Add `<LI>` entries to `<ul class="list-input settings-list">` for each new field
    - [ ] `./grademebutton/private/edit.js`
        - Add entry for each field to `GrademebuttonEdit`
    - [ ] `./grademebutton/private/edit.less`
        - Add styles to `.grademebutton_edit { }` block (if needed)
    - [ ] `./grademebutton/grademebutton.py`
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
