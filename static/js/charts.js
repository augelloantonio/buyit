$(document).ready(function(){
    var endpoint = 'charts/data/'

    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data){
            console.log(data)
        },
        error: function(error_data){
            console.log("error data")
            console.log(error_data)
        }
    })
})
