$( document ).ready(function() {
	$("button#getcols").click(getColors);
});


function getColors(){
    $.get("/get-colors", function(data, status){
        var cols = data.colors;
        var colorContainer = $('div#colors-container');
        $(colorContainer).empty();
        for(var i=0; i < cols.length; i++){
        	$(colorContainer).append('<div class="colpane" style="background-color:'+cols[i]+'"></div><br>');
        }
    });
}