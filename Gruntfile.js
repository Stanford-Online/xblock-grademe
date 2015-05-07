module.exports = function (grunt) {
    'use strict';

    var jshintrc = '.jshintrc';
    var gruntFile = 'Gruntfile.js';
    var directoryPackage = './grademebutton';
    var directoryPrivate = directoryPackage + '/private';
    var directoryPublic = directoryPackage + '/public';
    var directoryPrivateJsAll = directoryPrivate + '/**/*.js';
    var directoryPrivateLessAll = directoryPrivate + '/**/*.less';
    var directoryPrivateHtmlAll = directoryPrivate + '/**/*.html';
    var directoryPublicCssAll = directoryPublic + '/**/*.css';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        clean: [
            'node_modules/',
            '**/*.pyc',
        ],
        concat: {
            options: {
                separator: ';\n',
            },
            jsView: {
                src: [
                    directoryPrivate + '/view.js',
                ],
                dest: directoryPublic + '/view.js',
            },
            jsEdit: {
                src: [
                    directoryPrivate + '/edit.js',
                ],
                dest: directoryPublic + '/edit.js',
            },
            cssView: {
                src: [
                    directoryPrivate + '/view.less',
                ],
                dest: directoryPublic + '/view.less',
            },
            cssEdit: {
                src: [
                    directoryPrivate + '/edit.less',
                ],
                dest: directoryPublic + '/edit.less',
            },
        },
        copy: {
            images: {
                files: [
                    {
                        expand: true,
                        src: [
                            directoryPrivate + '/**/*.jpg',
                            directoryPrivate + '/**/*.png',
                            directoryPrivate + '/**/*.gif',
                        ],
                        dest: directoryPublic + '/',
                    },
                ],
            },
        },
        csslint: {
            dist: {
                src: [
                    directoryPublicCssAll,
                ],
            },
        },
        cssmin: {
            combine: {
                files: [{
                    footer: '\n',
                    expand: true,
                    cwd: directoryPublic,
                    src: [
                        '*.css',
                        '!*.min.css',
                    ],
                    dest: directoryPublic,
                    ext: '.min.css',
                }],
            },
        },
        htmlmin: {
            all: {
                options: {
                    removeComments: true,
                    removeCommentsFromCDATA: true,
                    collapseWhitespace: true,
                    collapseBooleanAttributes: true,
                    removeRedundantAttributes: true,
                    removeEmptyAttributes: true,
                },
                files: {
                    'grademebutton/public/edit.html': directoryPrivate + '/edit.html',
                    'grademebutton/public/view.html': directoryPrivate + '/view.html',
                },
            },
        },
        jshint: {
            options: {
                ignores: [
                ],
            },
            dist: [
                gruntFile,
                directoryPrivateJsAll,
            ],
        },
        less: {
            view: {
                options: {
                    sourceMap: true,
                    sourceMapFilename: 'grademebutton/public/view.less.min.css.map',
                    outputSourceFiles: true,
                    cleancss: true,
                    compress: true,
                },
                files: {
                    'grademebutton/public/view.less.min.css':
                        directoryPublic + '/view.less',
                },
            },
            edit: {
                options: {
                    sourceMap: true,
                    sourceMapFilename: 'grademebutton/public/edit.less.min.css.map',
                    outputSourceFiles: true,
                    cleancss: true,
                    compress: true,
                },
                files: {
                    'grademebutton/public/edit.less.min.css':
                        directoryPublic + '/edit.less',
                },
            },
        },
        uglify: {
            options: {
                footer: '\n',
                sourceMap: true,
            },
            combine: {
                files: [{
                    expand: true,
                    cwd: directoryPublic + '/',
                    src: [
                        '*.js',
                        '!*.min.js',
                    ],
                    dest: directoryPublic + '/',
                    ext: '.js.min.js',
                }],
            },
        },
        watch: {
            dist: {
                files: [
                    jshintrc,
                    gruntFile,
                    directoryPrivateJsAll,
                    directoryPrivateLessAll,
                    directoryPrivateHtmlAll,
                ],
                tasks: [
                    'default',
                ],
            },
        },
    });

    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-csslint');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-htmlmin');

    grunt.registerTask('default', [
        'jshint',
        'concat',
        'copy',
        'less',
        'csslint',
        'uglify',
        'htmlmin',
    ]);
};
