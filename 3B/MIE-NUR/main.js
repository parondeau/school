$(document).ready(function() {
	// setupMaps();
	setupClicks();
});

// function setupMaps() {
// 	var useragent = navigator.userAgent;
// 	var mapdiv = document.getElementById("map-canvas");

// 	if (useragent.indexOf('iPhone') != -1 || useragent.indexOf('Android') != -1 ) {
// 		mapdiv.style.width = '100%';
// 		mapdiv.style.height = '100%';
// 	} else {
// 		mapdiv.style.width = '600px';
// 		mapdiv.style.height = '800px';
// 	}
// 	var mapOptions = {
// 		center: { lat: 50.0833, lng: 14.4167},
// 		zoom: 15
// 	};
// 	var map = new google.maps.Map(mapdiv, mapOptions);
// }
function setupClicks() {
	$('#searchTab').on('click touchstart', function(){
		$('#tabBar *').removeClass('show');
		$('#searchTab *').addClass('show');
		$('#content > *').hide();
		$('#mainSearch').show();
	});
	$('#historyTab').on('click touchstart', function(){
		$('#tabBar *').removeClass('show');
		$('#historyTab *').addClass('show');
		$('#content > *').hide();
		$('#mainHistory').show();
	});
	$('#favTab').on('click touchstart', function(){
		$('#tabBar *').removeClass('show');
		$('#favTab *').addClass('show');
		$('#content > *').hide();
		$('#mainFav').show();
	});
	$('#listTab').on('click touchstart', function(){
		$('#tabBar *').removeClass('show');
		$('#listTab *').addClass('show');
		$('#content > *').hide();
		$('#mainList').show();
	});
	$('#mainSearch li').on('click', function(){
		$('#mainList').hide();
		$('#booking').show();
		$('.backButton').show();
	});
	$('.backButton').on('click', function(){
		$('#booking').hide();
		$('#mainList').show();
		$('.backButton').hide();
	});
}
