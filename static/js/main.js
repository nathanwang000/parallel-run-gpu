$("#add_task").click(function() {
    console.log('add task clicked')
    $.ajax({
	type: "POST",
	url: '/update_C'
    }).done(function(){
	//console.log('add_task_done')
    })
})
