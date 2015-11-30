// including plugins
// Make sure you run:
// npm install -g gulp 
// npm install gulp-less gulp-minify-css gulp-rename gulp-plumber
var gulp = require('gulp');
var less = require("gulp-less");
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var plumber = require('gulp-plumber');

// Task - Compile DNN Less Files

gulp.task('compile-dnn-less',function(){
    gulp.src('apps/less/apps.less')
    .pipe(plumber())
        .pipe(less())
        .pipe(gulp.dest('static/css'))
        .pipe(rename({
            suffix: '.min'
        }))
        .pipe(minifycss())
        .pipe(gulp.dest('static/css'));
});

// Task - Watches DNN less files

gulp.task('watch', function() {
    gulp.watch('static/less/**/*.less', ['compile-dnn-less']);
    gulp.watch('static/less/*.less', ['compile-dnn-less']);
    gulp.watch('apps/**/*.less', ['compile-dnn-less']);
});

// Task - 'Gulp' Command in terminal

gulp.task('default', ['compile-dnn-less', 'watch'], function() {});