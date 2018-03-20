var nameSpace = Anthem || {};

( function () {
	"use strict";
	
	var timeline;
	var wrapper, click_through, logo, copy, cta, width, height;
	
	nameSpace.init = function () {
		// Initialize any variables here
		wrapper = nameSpace.$( '#wrapper' );
		click_through = document.getElementById('click_through');
		width = 300;
		height = 250;


		wrapper.addClass( 'show' );

		nameSpace.initClickTag();
		nameSpace.initAnimation();

		if ( nameSpace.useFallback() ) {
			nameSpace.injectFallback();
		} else {
		nameSpace.startAnimation();
		}

		click_through.onmouseover = function () {	
		    TweenMax.to("#cta", 0.2, { y:-2, transformOrigin:"75% 60%", z:0.01, force3D:true, rotationZ: 0.01, transformPerspective: 400});
		};

		click_through.onmouseout = function () {
		    TweenMax.to("#cta", 0.2, {scale:1, force3D:true, z:0.01, rotationZ: 0.01, transformPerspective: 400, y:0});
		};

		
	};

	nameSpace.initClickTag = function () {
		click_through.onclick = function () {
			window.open( window.clickTag );
		};		
	};

	nameSpace.injectFallback = function() {
		var body = document.body;

		while ( body.firstChild ) {
			body.removeChild( body.firstChild );
		}

		var anchor = document.createElement('a');
		anchor.style.cursor = 'pointer';

		var img = new Image();
			img.src = './img/static.jpg';

		anchor.appendChild( img );
		anchor.onclick = function() { window.open(window.clickTag); };
		document.body.appendChild( anchor );
	};

	nameSpace.initAnimation = function () {
		// TweenMax can be used to set css
		// It will even take care of browser prefixes
		// TweenMax.set(logo, {x:100, y:50, opacity:0});

		timeline = new TimelineMax( {
			delay: 0.2,
			onComplete: nameSpace.onAnimationComplete
		} );

		timeline.pause();

		TweenMax.fromTo("#hero", 9, {scale:1}, {scale:1.25,z:0.01, force3D:true, rotationZ: 0.01, transformPerspective: 400});

		timeline.fromTo("#copy-1", 1, {autoAlpha:0}, {autoAlpha:1, z:0.01, force3D:true, rotationZ: 0.01, transformPerspective: 400, ease:Cubic.easeIn}, "+=0.5")
				.to("#copy-1", 1, {autoAlpha:0},"+=2.5")
				.fromTo("#copy-2", 1, {autoAlpha:0}, {autoAlpha:1, z:0.01, force3D:true, rotationZ: 0.01, transformPerspective: 400, ease:Cubic.easeIn}, "+=.2")
		
	};

	nameSpace.startAnimation = function () {
		// Code for animation		
		timeline.play();
	};

	nameSpace.onAnimationComplete = function () {
		// Log duration of timeline
		console.log( 'Animation Duration: ' + timeline.time() + 's' );

		// Show a CTA or any animations outside main timeline
		
	};
} ) ();