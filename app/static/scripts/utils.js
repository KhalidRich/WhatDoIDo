/*
* utils.js
* some front-end utilities to get the ball rolling
*/

var preference_types= ["#performing_arts", "#academic", "#sports", "#cultural", "#environmental", "#arts", "#gensex", "#stugovt","#media", "#political", "#religious", "#service", "#spinterest"];

var unpack_preferences = function(preferences) {
	for(var i = 0; i < preferences.length; i++) {
		if(preferences[i] === "1") { 
			$(preference_types[i]).attr('checked', true);
		}
	}
}

var init_form = function(data) {
	$(document).ready(function() {
		unpack_preferences(data);
	});
}