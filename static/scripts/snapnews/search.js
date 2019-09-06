$(document).ready(function () {
    $(".img").click(function () {
        $('#ZoomInTitle').text(this.children[1].value);
        $('.modal-body').html(this.children[2].value + "<br><img src=\"" + this.children[0].src + "\" height=\"720\" width=\"1280\">");
        $('#ZoomInModal').modal({});

    });
});

$(document).ready(function () {
    $('.table_main').click(function () {
        $(this.childNodes.item(3)).animate({height: "800px"})
    });
});


// 動態載入
let page_num = 0;
let channel;
let is_loading = false;
$(document).ready(function () {
    $('.channel_label').click(function () {
        let div = document.getElementById('result');
        channel = this.innerText;
        div.innerHTML = '';
        getData(channel, true)
    })
});


function getData(channel, init) {
    $("#preloading-modal").modal('show');
    if (init === true) {
        page_num = 0;
    }
    let div = document.getElementById('result');
    let para = window.location.href.split('?')[1];
    para += "&channel=" + channel + "&page_num=" + page_num;

    $.ajax({
        type: "GET",
        url: "/snapnews/GET/load_snapshot?" + para,
        success: function (response) {
            if (response.length === 0) {
                $("#preloading-modal").modal('hide');
                console.log('test');
                return
            }
            $.each(response, function (key, value) {
                div.innerHTML += "<img src=\"" + value.image + "\" height=\"180\" width=\"360\" onclick=\"trigger_modal(" + value.id + ")\">";

            });
            page_num += 1;
            if (div.scrollHeight === div.clientHeight) {

                getData(channel, false)
            }
            else {
                $("#preloading-modal").modal('hide');
            }


        }
    }).done(function () {
        is_loading = false;
    });


}

$(document).ready(function () {
    let result_div = document.getElementById('result');
    result_div.addEventListener('scroll', function () {

        if (result_div.scrollHeight - result_div.scrollTop - 10 < result_div.clientHeight) {

            if (is_loading === false) {
                is_loading = true;
                getData(channel, false)
            }

        }
    })
});


function trigger_modal(id) {
    let modal_body = document.getElementById("zoom-in-modal-body");
    let modal_title = document.getElementById('zoom-in-modal-label');
    let height = $(window).height() / 2;
    let width = $(window).width() / 2;
    $.ajax({
        type: "GET",
        url: "/snapnews/GET/load_single_snapshot?&idx=" + id,
        success: function (result) {

            modal_body.innerHTML = "<img src=\"" + result[0].image + "\" height=\"" + height + "\" width=\"" + width + "\">";
            let datetime = new Date(result[0].time);
            modal_title.innerText = datetime.toLocaleString()
        }
    });
    $("#zoom-in-modal").modal('show');
}

