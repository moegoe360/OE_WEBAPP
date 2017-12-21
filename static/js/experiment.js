/*
 * Checks if browser's screen changed, if it has, it runs the exitHandler method.
 */
if (document.addEventListener) 
{
    document.addEventListener('webkitfullscreenchange', exitHandler, false);
    document.addEventListener('mozfullscreenchange', exitHandler, false);
    document.addEventListener('fullscreenchange', exitHandler, false);
    document.addEventListener('MSFullscreenChange', exitHandler, false);
}

/*
 * exitHandler() checks if browser is fullscreen then manipulates HTML elements to disappear while leaving canvas, if not fullscreen, all the necessary HTML elements reappear. 
 */
function exitHandler()
{
    if (document.webkitIsFullScreen || document.mozFullScreen || document.msFullscreenElement !== null)
    {
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
		bd.style.backgroundColor = "black";
	}

    }
}
/*
 * ToggleFullScreen inputs the document page and uses this to check if browser is fullscreen or not. If browser is not fullscreen it changes to fullscreen, else it cancels fullscreen mode.
 */
function toggleFullScreen(elem) {		
    if ((document.fullScreenElement !== undefined && document.fullScreenElement === null) || (document.msFullscreenElement !== undefined && document.msFullscreenElement === null) || (document.mozFullScreen !== undefined && !document.mozFullScreen) || (document.webkitIsFullScreen !== undefined && !document.webkitIsFullScreen)) {
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

