'use strict';
angular.module('play').controller('MainCtrl',
	function ($scope) {

		$scope.stretchModes = [
			{label: "None", value: "none"},
			{label: "Fit", value: "fit"},
			{label: "Fill", value: "fill"}
		];

		$scope.config = {
			width: $(window).width(),
			height: $(window).height(),
			autoHide: true,
			autoHideTime: 3000,
			autoPlay: true,
			responsive: false,
			stretch: $scope.stretchModes[1],
			theme: {
				url: "/static/netflix_clone/lib/videogular/themes/default/videogular.css",
				playIcon: "&#xe000;",
				pauseIcon: "&#xe001;",
				volumeLevel3Icon: "&#xe002;",
				volumeLevel2Icon: "&#xe003;",
				volumeLevel1Icon: "&#xe004;",
				volumeLevel0Icon: "&#xe005;",
				muteIcon: "&#xe006;",
				enterFullScreenIcon: "&#xe007;",
				exitFullScreenIcon: "&#xe008;"
			}
		};
	}
);
