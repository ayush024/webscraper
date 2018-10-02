$(function(){
	$('#show').on('submit', function(e){
		e.preventDefault();
		$.ajax({
			url: $(tihs).attr('action'),
			method: $(this).attr('method')
			success: function(data){ $('').html(data)}
		});
	});	
});
