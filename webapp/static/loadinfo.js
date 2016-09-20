$('form.ajax').on('submit',function() {
    // To reference the current attribute
    var that = $(this),
        url = that.attr('action'),
        type = that.attr('method'),
        // To hold javascript object
        data = {};

    //Choosing selector name to find anything with an attribute name
    //Using each method to loop through all elements in the form
    that.find('[name]').each(function(index, value){
        // this References each of the input
        var that = $(this),
            name = that.attr('name'),
            value = that.val();
        // name refers to name of input field and value to its corresponding value
        data[name] = value;
     });
        console.log(data);

    $.ajax({
       url: '/register',
       //Type of request
       type:type,
       // Refers to all the information to be sent
       data:data,
       success: function(response){
            console.log(response);
       },
       error: function(response){
            alert('try more');
       }
     });
    return false;
});

