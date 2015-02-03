$(document).ready(function(){
	$(window).resize("resizeBackground");
		function resizeBackground(event) {
			var screenHeight = $(window).height();
			$('.events').height(screenHeight);
			$(".appsoc_trans_view").height(screenHeight);
		}
		resizeBackground();
});