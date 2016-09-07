/**
 * Created by Steven on 7/20/2016.
 */
$((function () {
    console.log("document loaded");
    $.ajax({
        url: '/loadMain',
        success: function (data) {
            data = jQuery.parseJSON(data);
            query = ''
            console.log(data[0][0]);
            for (i = 0; i < 10; i++) {
                for (j = 0; j < data[i].length; j++) {
                    query += data[i][j] + ', '
                }
                query = query.substring(0, query.length - 2);
                if (query.length == 0) {
                    query = 'No Matches!';
                }
                number = "#q" + (i+1);
                $(number).text(query);
                query = '';
            }

        },
        error: function (b) {
            console.log('failed')
        },
    });
}));