$(document).ready(function(){
    console.log('main loaded');
    $.ajax({
        url:"categories",
        success:function (myData, myStatus){
            console.log('my data', myData)
            myData.data.forEach(function(value) {
                $("#categories").append('<a>' + value + '</a>');
            });
        }
    });
});