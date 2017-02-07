var gulp = require('gulp')
var concat = require('gulp-concat')
var sourcemaps = require('gulp-sourcemaps')
var uglify = require('gulp-uglify')
var ngAnnotate = require('gulp-ng-annotate')
var cacheBuster = require('gulp-cache-bust');
var templateCache = require('gulp-angular-templatecache');
var gulpRename = require('gulp-rename');

gulp.task('favicon.ico', function() {
   gulp.src('favicon.ico')
   .pipe(gulp.dest('public'));
});

gulp.task('images', ['favicon.ico'], function() {
   gulp.src('images/*.png')
   .pipe(gulp.dest('public/images'));
});

gulp.task('css', ['images'], function () {
   return gulp.src(['styles/*.css', 'external/*.css'])
    .pipe(concat('style.min.css'))
    .pipe(gulp.dest('public'))
})

gulp.task('vendor', ['css'], function () {
  return gulp.src(['node_modules/angular/angular.min.js',
                   'node_modules/angular-route/angular-route.min.js',
                   'node_modules/jssha/src/sha.js',
                   'node_modules/angular-base64/angular-base64.min.js',
                   'node_modules/angular-local-storage/dist/angular-local-storage.min.js',
                   'node_modules/angular-smart-table/dist/smart-table.min.js',
                   'node_modules/angular-animate/angular-animate.min.js',
                   'node_modules/angular-sanitize/angular-sanitize.min.js',
                   'external/ui-bootstrap-tpls-1.3.2.min.js'])
    .pipe(sourcemaps.init())
      .pipe(concat('vendor.js'))
      .pipe(ngAnnotate())
      //.pipe(uglify())
    //.pipe(sourcemaps.write())
    .pipe(gulp.dest('public'));
})

gulp.task('js', ['vendor'], function () {
  return gulp.src(['modules/**/*.js', 'modules/**/*.js'])
    .pipe(sourcemaps.init())
      .pipe(concat('app.js'))
      .pipe(ngAnnotate())
    .pipe(gulp.dest('public'));
})

gulp.task('templates', ['js'], function () {
  return gulp.src(['modules/components/*/views/*.html',
                   'modules/home/views/*.html',
                   'modules/authentication/views/*.html'])
       .pipe(templateCache({ module:'templates', standalone:true }))
    .pipe(gulp.dest('public'));
});

gulp.task('renameIndex', ['templates'], function () {
    return gulp.src('index.html')
        .pipe(gulpRename('index.html'))
        .pipe(gulp.dest('public'));
});

// cacheBuster looks at the css and js files and appends a hash to the
// request to cause the file to get reloaded when the file changes.
gulp.task('cacheBuster', ['renameIndex'], function () {
    return gulp.src('public/index.html')
        .pipe(cacheBuster())
        .pipe(gulp.dest('public'));
});

gulp.task('default', ['cacheBuster']);


