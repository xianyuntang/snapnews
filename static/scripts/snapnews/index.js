// 選取日期

$(document).ready(function () {
    $('#start').datepicker({
        language: 'zh'
    });
    $('#end').datepicker({
        language: 'zh'
    });
});

$(document).ready(function () {
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1;
    let yyyy = today.getFullYear();

    if (dd < 10) {
        dd = '0' + dd;
    }

    if (mm < 10) {
        mm = '0' + mm;
    }

    today = yyyy + '-' + mm + '-' + dd;
    $('#StartTime').val(today);
    $('#EndTime').val(today);

});


$.ajax({
    type: "GET",
    url: "/snapnews/GET/generate_word_cloud_today_only/",
    success: function (result) {
        let words = [];
        let today = new Date();
        let dd = today.getUTCDate();
        let mm = today.getUTCMonth() + 1;
        let yyyy = today.getUTCFullYear();

        if (dd < 10) {
            dd = '0' + dd;
        }

        if (mm < 10) {
            mm = '0' + mm;
        }

        today = yyyy + '-' + mm + '-' + dd;
        $.each(result, function (key, value) {
            words.push({
                text: key,
                weight: Math.log10(value),
                link: "/snapnews/search?keyword=" + key + "&start=" + today + "&end=" + today
            });


        });
        $('#wordcloud_today').jQCloud(words, {
            autoResize: true,
            colors: ["#EA526F", "#F1E8B8", "#FF8A5B", "#25CED1", "#F9DF74", "#CCFF66", "#FFFFFF"]
        });
    }
});


$.ajax({
    type: "GET",
    url: "/snapnews/GET/generate_word_cloud/",
    success: function (result) {
        let words = [];
        let today = new Date();
        let dd = today.getDate();
        let mm = today.getMonth() + 1;
        let yyyy = today.getFullYear();

        if (dd < 10) {
            dd = '0' + dd;
        }

        if (mm < 10) {
            mm = '0' + mm;
        }

        $.each(result, function (key, value) {

            words.push({
                text: key,
                weight: Math.log10(value)
            });


        });

        $('#wordcloud_all').jQCloud(words, {
            autoResize: true,
            colors: ["#EA526F", "#F1E8B8", "#FF8A5B", "#25CED1", "#F9DF74", "#CCFF66", "#FFFFFF"]
        });
    }
});

// $(document).ready(function getBreakingNews() {
//     $.ajax({
//         type: "GET",
//         url: "/snapnews/GET/breaking_news/",
//         success: function (result) {
//             $.each(result, function (key, value) {
//                 $.toast({
//                     heading: value.keyword,
//                     text: value.time + "<br><img src=\"" + value.image + "\" height=\"180\" width=\"360\">",
//                     position: 'bottom-right',
//                     hideAfter: 60000,
//                     stack: 3,
//                     loader: true,        // Change it to false to disable loader
//                     loaderBg: '#9EC600'  // To change the background
//                 });
//             });
//
//
//         },
//         complete: function () {
//
//             //setTimeout(getBreakingNews, 2000);
//
//
//         }
//
//     });
// });

// 向左向右文字雲
function moveToLeft() {
    $('.next').show();
    $('.prev').hide();
    $('.wordcloud-container').animate({
        left: "0%"
    });
}

function moveToRight() {
    $('.prev').show();
    $('.next').hide();
    $('.wordcloud-container').animate({
        left: "-100%"
    });
}
