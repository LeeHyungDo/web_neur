setInterval(function loadImg() {
	var xhttp;
	if(window.XMLHttpRequest){
		xhttp = new XMLHttpRequest();
	}else{
		xhttp= new ActiveXObject("Microsoft.XMLHTTP");
	}
	xhttp.onreadystatechange = function() {
		if(xhttp.readyState == 4 && xhttp.status == 200){
			document.getElementById("conved").innerHTML= xhttp.responseText;
		}
	};
	xhttp.open("get", "/project/imge/", true);
	xhttp.send();
}, 3000);
