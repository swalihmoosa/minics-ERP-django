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

    count = parseInt(document.getElementById("count").value)
    total = parseInt(document.getElementById("total").value)
    product_price = parseInt(document.getElementById("product_price").value)

    pk = document.getElementById("count").name
    plus = document.getElementById("plus")
    minus = document.getElementById("minus")

    document.getElementById("total").value = count * product_price
    
    $(plus).on('click', function(){
        count = count + 1
        document.getElementById("count").value = count
        document.getElementById("total").value = count * product_price
        console.log(product_price);
    })

    $(minus).on('click', function(){
        count = count - 1
        document.getElementById("count").value = count
    })

})

