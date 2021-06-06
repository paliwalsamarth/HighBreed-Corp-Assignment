
function handleForm(handle_func){

    $("#submitBtn").attr("disabled", true);
    $('#submitBtnInitial').hide();
    $('#submitBtnLoad').show();

    var serializedData = $('#form').serialize();
    // console.log(serializedData);
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: $('#formURL').attr('value'),
            data: serializedData,
            success: function (response) {
                // console.log(response);
                handleResponse(response,handle_func);
            },
            error: function (response) {
                // alert the error if any error occured
                console.log("error : ",response);
                handleError();
            }
        })
}

function handleResponse(data, handle_func){
	if (data.status) {
        var icon = 'error';
        if(data.status == 'success'){icon = 'success'}
        // console.log(data);
        mytoaster(data.message,icon);
		handle_func(data);
        $("#submitBtn").attr("disabled", false);
        $('#submitBtnInitial').show();
        $('#submitBtnLoad').hide();
    }
	else{
		handleError();
	}
}

function handleError(){
    mytoaster("Invalid Request",'error');
    $("#submitBtn").attr("disabled", false);
    $('#submitBtnInitial').show();
    $('#submitBtnLoad').hide();
}