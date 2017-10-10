function toggleFullScreen(elem) {
		var x = document.getElementById("exam");
		var y = document.getElementById("navbar");
		var btn = document.getElementById("btnFullScreen");
		var bd = document.body;
		if (x.style.display === "none" && y.style.display === "none") {
			x.style.display = "block";
			y.style.display = "block";
			btn.style.float = "none";
			btn.style.opacity = "1";
			bd.style.backgroundColor = "white";
		} else {
			x.style.display = "none";
			y.style.display = "none";
			btn.style.float = "left";
			btn.style.opacity = "0.1";
			bd.style.backgroundColor = "black";
		}
		
		
		
		
    if ((document.fullScreenElement !== undefined && document.fullScreenElement === null) || (document.msFullscreenElement !== undefined && document.msFullscreenElement === null) || (document.mozFullScreen !== undefined && !document.mozFullScreen) || (document.webkitIsFullScreen !== undefined && !document.webkitIsFullScreen)) {
    	//nv.remove();
    	if (elem.requestFullScreen) {
            elem.requestFullScreen();
        } else if (elem.mozRequestFullScreen) {
            elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullScreen) {
            elem.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
        } else if (elem.msRequestFullscreen) {
            elem.msRequestFullscreen();
        }
    } else {
    	//nv.add();
        if (document.cancelFullScreen) {
            document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        }
    }
}