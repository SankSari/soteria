function load() {
	  var output = document.getElementById("out");

	  var latitude, longitude;

	  if (!navigator.geolocation){
	    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
	    return;
	  }

	  function success(position) {
	    var latitude  = position.coords.latitude;
	    var longitude = position.coords.longitude;

	    output.innerHTML = '<p>Latitude is ' + latitude + '° <br>Longitude is ' + longitude + '°</p>';

	    var img = new Image();
	    img.src = "https://atlas.microsoft.com/map/static/png?subscription-key=LY0GZYlXEeD9A8PFBV1yhNL0VBDhDGYl4_GfhOdpnBw&api-version=1.0&layer=basic&style=main&zoom=16&height=512&width=512&center=" + longitude + "," + latitude;

	    output.appendChild(img);
	  }

	  function error() {
	    output.innerHTML = "Unable to retrieve your location";
	  }

	  output.innerHTML = "<p>Locating…</p>";
	  navigator.geolocation.getCurrentPosition(success, error);

	  return latitude, longitude;
	}

	window.onload = function(e) {
		load();
	}