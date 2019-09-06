let add_keyword_group = function () {

    let keyword_group = document.getElementById('add-keyword-group').value;
    let data = {'keyword_group': keyword_group};
    $.ajax({
            method: "POST",
            url: "/account/POST/add_keyword_group",
            data: data
        }
    ).then(function () {
        window.location.reload();
    })
};

let mod_keyword_group = function (keyword_group_id) {
    let keyword_group_name = document.getElementById('keyword-group-title-' + keyword_group_id);
    keyword_group_name.disabled = false;
    keyword_group_name.addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {


            let data = {
                'keyword_group_id': keyword_group_id,
                'keyword_group_name': keyword_group_name.value
            };
            $.ajax({
                method: "POST",
                url: "/account/POST/mod_keyword_group",
                data: data,
                dataType: "json"
            }).then(function () {
                keyword_group_name.disabled = true;
            })
        }

    })


};

let del_keyword_group = function (keyword_group_id) {
    let keyword_group = document.getElementById('keyword-group-' + keyword_group_id);
    let data = {'keyword_group_id': keyword_group_id};
    $.ajax({
        method: "POST",
        url: "/account/POST/del_keyword_group",
        data: data,
        dataType: "json"
    }).then(function () {
        keyword_group.parentNode.removeChild(keyword_group)

    });
};

let del_keyword = function (elem, keyword_type, keyword_group_id, keyword) {
    let data = {
        'keyword_group_id': keyword_group_id,
        'keyword': keyword,
        'keyword_type': keyword_type
    };
    $.ajax({
        method: "POST",
        url: "/account/POST/del_keyword",
        data: data,
        dataType: "json"
    }).then(function () {
        elem.parentNode.parentNode.removeChild(elem.parentNode);
    })
};

let add_keyword = function (keyword_type, keyword_group_id) {
    let keyword_group;
    let keyword_group_add_btn;
    if (keyword_type === 'inclusive') {
        keyword_group = document.getElementById('keyword-group-' + keyword_group_id).childNodes[3].childNodes[1].childNodes[3];
        keyword_group_add_btn = document.getElementById('keyword-group-' + keyword_group_id).childNodes[3].childNodes[1].childNodes[3].lastChild.previousSibling;

    } else {
        keyword_group = document.getElementById('keyword-group-' + keyword_group_id).childNodes[3].childNodes[3].childNodes[3];
        keyword_group_add_btn = document.getElementById('keyword-group-' + keyword_group_id).childNodes[3].childNodes[3].childNodes[3].lastChild.previousSibling;

    }


    console.log(keyword_group_add_btn);
    let keyword_input = document.createElement('input');
    keyword_input.className = "new-keyword-input form-control";
    keyword_input.addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            let data = {
                'keyword_group_id': keyword_group_id,
                'keyword': keyword_input.value,
                'keyword_type': keyword_type
            };
            $.ajax({
                method: "POST",
                url: "/account/POST/add_keyword",
                data: data,
                dataType: "json"
            }).then(function () {

                let keyword_div = document.createElement('div');
                keyword_div.className = 'keyword';
                keyword_div.innerText = keyword_input.value + " ";
                let keyword_del_btn = document.createElement('button');
                keyword_del_btn.innerHTML = "&#xf00d;";
                keyword_del_btn.className = "fas btn-icon";
                keyword_del_btn.type = "button";
                keyword_del_btn.onclick = function () {
                    del_keyword(this, keyword_type, keyword_group_id, keyword_input.value);
                };
                keyword_group_add_btn.hidden = false;
                keyword_div.appendChild(keyword_del_btn);
                keyword_group.insertBefore(keyword_div, keyword_group.lastChild.previousSibling);
                keyword_group.removeChild(keyword_input);
            })
        }


    });

    keyword_group_add_btn.hidden = true;
    keyword_group.insertBefore(keyword_input, keyword_group.lastChild.previousSibling);
    keyword_input.focus();

};

