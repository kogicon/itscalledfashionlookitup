$( document ).ready(function() {
	$("button#getcols").click(getColors);
});


function getColors(){
    $.get("/get-colors", function(data, status){
        var cols = data.colors;
        var divs = $('div.colpane')
        for(var i=0; i < cols.length && i < divs.length; i++){
			$(divs[i]).css('background-color', cols[i]);
        }
    });
}