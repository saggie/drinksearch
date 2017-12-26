$(document).ready(function(){
    console.log('main loaded');
    $.ajax({
        url:"categories",
        success:function (myData, myStatus){
            console.log('categories', myData);
            myData.data.forEach(function(value) {
                $('#categories').append('<a>' + value + '</a>');
            });

            $('a', '#categories').on('click', function(data) {
                alert(data);
            });

        }
    });
    loadDrinks(null);
});

function loadDrinks(category) {
/*    $.ajax({
        url:"drinks",
        success:function (myData, myStatus){
            console.log('drinks', myData);
            if (category != null) {
                console.log('filter by category');
            }
            $('#drinks').DataTable();
        }
    });
*/
    $('#drinks').DataTable({
        ajax: 'drinks'
    });


}
