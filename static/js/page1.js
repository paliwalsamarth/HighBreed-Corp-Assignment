console.log("page1 js running");

$("input[name=storeName]").change(function () {
    if(this.value == "android")
    {
        $("#id_appID").attr("required", true);
        $("#id_appName").attr("required", false);

        if($('#appIDdiv').css('display') == 'none'){
            $("#appIDdiv").show();
        };

        if($('#appNamediv').css('display') != 'none'){
            $("#appNamediv").hide();
        };
    }
    else if(this.value == "apple")
    {
        $("#id_appID").attr("required", true);
        $("#id_appName").attr("required", true);

        if($('#appIDdiv').css('display') == 'none'){
            $("#appIDdiv").show();
        };

        if($('#appNamediv').css('display') == 'none'){
            $("#appNamediv").show();
        };
    }
    else{
        $("#appIDdiv").hide();
        $("#appNamediv").hide();
        $("#id_appID").attr("required", false);
        $("#id_appName").attr("required", false);
    }
});

const form = document.getElementById('form');

form.addEventListener('submit', function(event){
    event.preventDefault();
    handleForm(handle_app);
});

function handle_app(data){
    if(data.name){
        if(data.storeName == 'apple'){
            if($('#outputAppDownDiv').css('display') != 'none'){
                $("#outputAppDownDiv").hide();
            };
        }
        else{
            if($('#outputAppDownDiv').css('display') == 'none'){
                $("#outputAppDownDiv").show();
            };
            $('#outputAppNOfDown').text(data.nOfDown);
        }
        $('#outputAppName').text(data.name);
        $("#outputAppImg").attr("src", data.icon);
        $('#outputAppDevName').text(data.dev_name);
        $("#outputAppDevLink").attr("src", data.dev_link);
        $('#outputAppDesc').text(data.desc);
        $('#outputAppRate').text(data.rating);
        $('#outputAppNOfReview').text(data.nOfReview);
        $("#outputAppInfoCard").css("visibility", "visible");
        $("#form").trigger('reset');
    }

}
