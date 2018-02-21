
$(document).ready(function(){  
    $("i").hide();
    $("button").click(function(e){
        e.preventDefault()
        var get_name = $(this).attr('id');
        var N = 10; // Assuming sector never contains more than N branches        
        for (j=0;j<N;j++) {
            var name = '#'.concat(get_name).concat("branche").concat(j);
            console.log(name)
            $(name).toggle();
        }        
    });

});

$('#sector-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    begin_page_2();
});

// AJAX for posting
function begin_page_2() {
    console.log("grading is working!") // sanity check
    var form_id = $('#sector-form').val();
    $.ajax({
        url : "begin_page_2/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#sector-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#sector-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
});