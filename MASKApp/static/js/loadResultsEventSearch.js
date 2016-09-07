/**
 * Created by Steven on 7/19/2016.
 */
$(function () {
    $('#').click(function () {

        $.ajax({
            url: '/loadResultsEventSearch',
            data: $('form').serialize(),
            type: 'POST',
            success: function (data) {
                //open a new window note:this is a popup so it may be blocked by your browser
                var newWindow = window.open("", "new window", "width=200, height=100");

                //write the data to the document of the newWindow
                newWindow.document.write(data);
            }
        });
    });
});