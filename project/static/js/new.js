// var map; 
// function doFirst(){
// 	navigator.geolocation.getCurrentPosition(succCallback);
// }

// function succCallback(arg){
// 	// var lati = arg.coords.latitude;
// 	// var longi = arg.coords.longitude;
			
// 	//中心點
// 	var lati = 34.9948561;
// 	var longi = 135.7850463;

// 	var xy = new google.maps.LatLng(lati, longi);
// 	var mapBoard = document.getElementById('mapBoard');
// 	var options = {
// 		zoom: 14,
// 		center: xy,
// 		mapTypeId: google.maps.MapTypeId.ROADMAP
// 	};
// 	map = new google.maps.Map(mapBoard, options);
// 	var marker = new google.maps.Marker({ 
// 		position: xy, 
// 		map: map,
//         icon:'https://maps.google.com/mapfiles/kml/shapes/library_maps.png' 
// 	});
// 	marker.setTitle('目前位置'); 
// }

// function showInfo(shop){
// 	switch(shop.id){
// 		case 'res':
// 			getLocation(res, '找餐廳');
// 			break; 
// 		case 'site':
// 			getLocation(site, '找景點');
// 			break ; 
// 		case 'shopping':
// 			getLocation(shopping, '購物去');
// 			break ;
// 		case 'hotel':
// 			getLocation(hotel, '找飯店');
// 			break ;
//         case 'activity':
// 			getLocation(activity, '活動');
// 			break ;
//         case 'wearing':
// 			getLocation(wearing, '衣著');
// 			break ;
// 	}
// }
// var markers = new Array(); 
// function getLocation(as,title){
// 	var i = 0;
// 	for(var k in markers){
// 		markers[k].setVisible(false);
// 	}
// 	for(var k in as){
// 		var lati = as[k].split(',')[0]; 
// 		var longi = as[k].split(',')[1]; 
// 		var xy = new google.maps.LatLng(lati, longi);
// 		var marker = new google.maps.Marker({ 
// 			position: xy, 
// 			map: map,
//             icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png' 
// 		});
// 		marker.setTitle(title); 
// 		markers[i]  = marker;i++ ;           
// 	}           
// }

// window.addEventListener('load',doFirst,false);

