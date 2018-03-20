var nameSpace = Test || {};

( function () {
	"use strict";
	
	var timeline;
	var wrapper, clickThrough, logo, copy, cta, width, height;
	
	nameSpace.init = function () {
		// Initialize any variables here
		wrapper = nameSpace.$( '#wrapper' );
		clickThrough = document.getElementById('click_through');
		logo = nameSpace.$( '#logo' );
		copy = nameSpace.$( '#copy' );
		cta = nameSpace.$( '#cta' );
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
	};

	nameSpace.initClickTag = function () {
		clickThrough.onclick = function () {
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
		
		timeline.add( [
			TweenMax.to( logo, 0.6, {opacity: 1} ),
			TweenMax.to(copy, 0.8, { css:{opacity: 1}, delay:0.4 } )
		] );
	};

	nameSpace.startAnimation = function () {
		// Code for animation		
		timeline.play();
	};

	nameSpace.onAnimationComplete = function () {
		// Log duration of timeline
		console.log( 'Animation Duration: ' + timeline.time() + 's' );

		// Show a CTA or any animations outside main timeline
		TweenMax.from( cta, 0.4, { y: '110%' } );
		TweenMax.to( cta, 0.4, { opacity: 1 } );
	};
} ) ();