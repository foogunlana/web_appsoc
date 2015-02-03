$(document).ready(function(){
	$(window).resize("resizeBackground");
		function resizeBackground(event) {
			var screenHeight = $(window).height();
			$(".appsoc_trans_view").height(screenHeight);
		}
		resizeBackground();
});