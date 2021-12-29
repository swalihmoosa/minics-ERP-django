// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

$(document).ready(function(){

    $("form.subscribe").on("submit", function(event){
        event.preventDefault();
        var $this = $(this);

        var url = $this.attr("action")
        var method = $this.attr("method")

        jQuery.ajax({
            type : method,
            url : url,
            dataType : "json",
            data : new FormData(this),
            processData : false,
            contentType : false,
            cache : false,

            success : function(data){
                var title = data["title"]
                var text = data["message"]
                var status = data["status"]

                Swal.fire({
                    icon: status,
                    title: title,
                    text : text
                })
                  
                if (status == "success"){
                    $this.trigger("reset");
                }
            },
            error : function(data){

            }
        })
    })
})