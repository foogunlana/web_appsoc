$(document).ready(function(){
	$(window).resize("resizeBackground");
		function resizeBackground(event) {
			var screenHeight = $(window).height();
			$('.events').height(screenHeight);
		}
		resizeBackground();
});