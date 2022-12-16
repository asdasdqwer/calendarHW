allElements = document.getElementsByClassName("select");

for (var i = 0; i < allElements.length; i++) {
    allElements[i].onclick = function () {
        $.ajax({
            type: "POST",
            url: "",
    
            data: {
                stufe: this.id.replace("s", ""),
                csrfmiddlewaretoken: window.CSRF_TOKEN
            },
    
            success: function(html) {
                window.open("/homework", "_self");
            }
        });
    }
}