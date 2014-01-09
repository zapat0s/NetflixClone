'use strict';


// Declare app level module which depends on filters, and services
angular.module('netflixClone', [
    'ngRoute',
    'ui.bootstrap',
    //'ngAnimate',
    'netflixClone.services',
    'netflixClone.controllers'
])
.config(['$routeProvider', 'netflixCloneConfig', function($routeProvider, netflixCloneConfig) {
    //$routeProvider.when('/', {
    //    templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/index.html',
    //    controller: 'IndexCtrl'
    //});
    
    $routeProvider.when('/movies', {
        templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/grid.html',
        controller: 'MovieListCtrl'
    });
    $routeProvider.when('/movies/:genre', {
        templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/grid.html',
        controller: 'MovieListCtrl'
    });
    $routeProvider.when('/movies/detail/:movieId', {
        templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/movieDetail.html',
        controller: 'MovieDetailCtrl'
    });
    
    $routeProvider.when('/tvshows', {
        templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/grid.html',
        controller: 'TvShowListCtrl'
    });
    $routeProvider.when('/tvshows/:genre', {
        templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/grid.html',
        controller: 'TvShowListCtrl'
    });
    $routeProvider.when('/tvshows/detail/:tvShowId', {
        templateUrl: netflixCloneConfig.static_url + '/netflix_clone/partials/tvshowDetail.html',
        controller: 'TvShowDetailCtrl'
    });
    
    $routeProvider.otherwise({redirectTo: '/movies'});
}]);
