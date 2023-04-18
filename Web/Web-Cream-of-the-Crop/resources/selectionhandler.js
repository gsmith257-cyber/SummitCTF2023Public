function postHandler()
{
    try{
	event.preventDefault();
	var flavor = $("#favoriteicecream").val();
	var xml = 
	`<?xml version="1.0" encoding="ISO-8859-1"?>
	<icecream>
	<flavor>${flavor}</flavor>
	</icecream>`
	var data = btoa(xml);
	}
    catch(error){
	console.log('Error:', error);
}
$.ajax({
	type: 'POST',
	url: 'selection.php',
	data: {"data":data},
	});
       } 
