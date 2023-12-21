$( document ).ready(function() {
    $("#subset_accs").find(".accordion-item").hide()
    $("#subset_by").on("change",function(){
        var selected_list = $(this).find("option:selected").toArray().map((x)=>x.text)
        $("#subset_accs").find(".accordion-item").toArray().map(
            function(x){
                if (selected_list.indexOf($(x).data("value"))>-1) {
                    $(x).show()
                } else {
                    $(x).hide()
                }
            })
        })
});