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

count = parseInt(document.getElementById("count").value)
total = parseInt(document.getElementById("total").value)
product_price = parseInt(document.getElementById("product_price").value)

pk = document.getElementById("count").name
plus = document.getElementById("plus")
minus = document.getElementById("minus")

subtotal = parseInt(document.getElementById("subtotal").value)
shipping = parseInt(document.getElementById("shipping").value)
tax = parseInt(document.getElementById("tax").value)
grant_total = parseInt(document.getElementById("grant_total").value)

document.getElementById("total").value = count * product_price
document.getElementById("subtotal").value = document.getElementById("total").value
document.getElementById("tax").value = document.getElementById("total").value *6/100
document.getElementById("grant_total").value = parseInt(document.getElementById("total").value) + parseInt(document.getElementById("shipping").value) + parseInt(document.getElementById("tax").value)

function plus_count(){
    count = count + 1
    document.getElementById("count").value = count
    document.getElementById("total").value = count * product_price
    document.getElementById("subtotal").value = document.getElementById("total").value
    document.getElementById("tax").value = document.getElementById("total").value *6/100
    document.getElementById("grant_total").value = parseInt(document.getElementById("total").value) + parseInt(document.getElementById("shipping").value) + parseInt(document.getElementById("tax").value)


}

function minus_count(){
    count = count - 1
    document.getElementById("count").value = count
    document.getElementById("total").value = count * product_price
    document.getElementById("subtotal").value = document.getElementById("total").value
    document.getElementById("tax").value = document.getElementById("total").value *6/100
    document.getElementById("grant_total").value = parseInt(document.getElementById("total").value) + parseInt(document.getElementById("shipping").value) + parseInt(document.getElementById("tax").value)


}

// function add(){
//     console.log("click plus");
// }