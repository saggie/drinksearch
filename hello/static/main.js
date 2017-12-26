$(document).ready(function(){
    console.log('main loaded');
    $.ajax({
        url:"categories",
        success:function (myData, myStatus){
            console.log('categories', myData);
            myData.data.forEach(function(value) {
                $('#categories').append('<a data-category="' + value + '">' + value + '</a>');
            });

            $('a', '#categories').on('click', function(event) {
                var category = $(event.target).data('category');
                console.log('category is clicked', category);
                loadDrinks(category);
            });

        }
    });
    loadDrinks();
});

var table = null;

function loadDrinks(category) {
    var query = 'drinks';
    if (category != null && category != '*') {
        query += '?category=' + encodeURIComponent(category);
    }
    console.log('query', query);

    if (table == null) {
        table = $('#drinks').DataTable({
            ajax: query,
            pageLength: 20
        });
    }
    else {
        table.ajax.url(query).load();
    }
}
