'use strict';

/* Controllers */

angular.module('netflixClone.controllers', [])
    .controller('MovieDropdownCtrl', ['$scope', 'Movie',
        function MovieDropdownCtrl($scope, Movie) {
        
        $scope.items = Movie.query(function(items) {
        
            // Create genre list
            $scope.genres = new Array();
            for(var i = 0; i < $scope.items.length; i++) {
                $scope.genres = $scope.genres.concat($scope.items[i].genre_tags);
            }
            
            // Remove duplicates
            for(var i = 0; i < $scope.genres.length; ++i) {
                for(var j = i + 1; j < $scope.genres.length; ++j) {
                    if($scope.genres[i] === $scope.genres[j])
                        $scope.genres.splice(j--, 1);
                }
            }
        });
    }])
    .controller('MovieListCtrl', ['$scope', '$routeParams', 'Movie',
        function MovieListCtrl($scope, $routeParams, Movie) {
        
        // Set Page Title
        $(document).attr('title', 'NetflixClone - Movies');

        // Set active highlight on Movies in Navbar
        $("#movieDropdown").addClass('active');
        $("#tvshowDropdown").removeClass('active');
        
        // basePath to create urls with
        $scope.basePath = '/movies';
        
        $scope.items = Movie.query();
        
        $scope.orderProp = 'title';
        
        $scope.filterByGenre = function(movie) {
            if($routeParams.genre == null) {
                return true;
            }
            for(var i = 0; i < movie.genre_tags.length; i++) {
                if(movie.genre_tags[i] == $routeParams.genre) {
                    return true;
                }
            }
            return false;
        }

    }])
    
    .controller('MovieDetailCtrl', ['$scope', '$routeParams', 'Movie',
        function MovieDetailCtrl($scope, $routeParams, Movie) {
    
        // Set active highlight on Movies in Navbar
        $("#movieDropdown").addClass('active');
        $("#tvshowDropdown").removeClass('active');
        
        $scope.basePath = "/movies";
        
        // Get movie from service
        $scope.item = Movie.get({movieId: $routeParams.movieId}, function(item) {
            $(document).attr('title', 'NetflixClone - ' + item.title);
        });
    }])
    .controller('TvShowDropdownCtrl', ['$scope', 'TvShow',
        function TvShowDropdownCtrl($scope, TvShow) {
        
        $scope.items = TvShow.query(function(items) {
        
            // Create genre list
            $scope.genres = new Array();
            for(var i = 0; i < $scope.items.length; i++) {
                $scope.genres = $scope.genres.concat($scope.items[i].genre_tags);
            }
            
            // Remove duplicates
            for(var i = 0; i < $scope.genres.length; ++i) {
                for(var j = i + 1; j < $scope.genres.length; ++j) {
                    if($scope.genres[i] === $scope.genres[j])
                        $scope.genres.splice(j--, 1);
                }
            }
        });
    }])
    .controller('TvShowListCtrl', ['$scope', '$routeParams', 'TvShow',
        function TvShowListCtrl($scope, $routeParams, TvShow) {
        
        // Set Page Title
        $(document).attr('title', 'NetflixClone - TV Shows');
    
        // Set active highlight on TV Shows in Navbar
        $("#tvshowDropdown").addClass('active');
        $("#movieDropdown").removeClass('active');
        
        // basePath to create urls with
        $scope.basePath = '/tvshows';
        
        $scope.items = TvShow.query();
        
        $scope.filterByGenre = function(tvshow) {
            if($routeParams.genre == null)
                return true;		
            for(var i = 0; i < tvshow.genre_tags.length; i++) {
                if(tvshow.genre_tags[i] == $routeParams.genre) {
                    return true;
                }
            }
            return false;
        }
    
    }])
    .controller('TvShowDetailCtrl', ['$scope', '$routeParams', 'TvShow',
        function TvShowDetailCtrl($scope, $routeParams, TvShow) {
    
        // Set active highlight on TV Shows in Navbar
        $("#tvshowDropdown").addClass('active');
        $("#movieDropdown").removeClass('active');
        
        $scope.basePath = "/tvshows";
        
        // Get movie from service
        $scope.item = TvShow.get({tvShowId: $routeParams.tvShowId}, function(item) {
            $(document).attr('title', 'NetflixClone - ' + item.title);
        });
    }]);
