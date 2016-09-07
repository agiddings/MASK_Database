/**
 * Created by Steven on 7/18/2016.
 */
$(function () {
    $('#btnSignUp').click(function () {

        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});