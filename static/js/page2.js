console.log("page2 js running");


const form = document.getElementById('form');

form.addEventListener('submit', function(event){
    event.preventDefault();
    handleForm(handle_key);
});

function handle_key(data){
    
        $('#nOfURL').text(data.nOfURL);

    if(data.inputKeywords && data.outputKeywords){
        
            $('#myModalNOfIn').text(data.inputKeywords.length);
            $('#myModalNOfOut').text(data.outputKeywords.length);
            if(data.inputKeywords.length == 0){
                $('#myModalTitle').text("No keywords. Bad Luck !");
                $('#pasteInputKeywords').text("Nothing here");
                $('#pasteOutputKeywords').text("Nothing here. Input site had no keywords to compare !");    
            }else if(data.outputKeywords.length == 0){
                $('#myModalTitle').text("Hey, I found some keywords");
                $('#pasteInputKeywords').text(data.inputKeywords.join(', '));
                $('#pasteOutputKeywords').text("Nothing here. Please add more related links then retry !");    
            }else{
                $('#myModalTitle').text("Hey, I found some keywords");
                $('#pasteInputKeywords').text(data.inputKeywords.join(', '));
                $('#pasteOutputKeywords').text(data.outputKeywords.join(', '));
            }
            $('#myModal').modal(focus);
            $("#form").trigger('reset');
    }
        


}