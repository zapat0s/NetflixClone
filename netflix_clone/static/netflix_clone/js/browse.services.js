'use strict';

/* Services */

angular.module('netflixClone.services', ['ngResource'])
    .constant('netflixCloneConfig', {
        version: '0.1 alpha',
        api_url: '/api',
        static_url: '/static',
        media_url: '/media',
        play_url: '/play',
        logout_url: '/auth/logout'
     })
    .factory('Movie', ['$resource', 'netflixCloneConfig',
        function ($resource, netflixCloneConfig) {
            return $resource(netflixCloneConfig.api_url + '/movies/:movieId.json');
            }])
    .factory('TvShow', ['$resource', 'netflixCloneConfig',
        function ($resource, netflixCloneConfig) {
            return $resource(netflixCloneConfig.api_url + '/tvshows/:tvShowId.json');
            }]);
