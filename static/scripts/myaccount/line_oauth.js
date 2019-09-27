let get_line_api_key = function () {
    let client_id = 'xBhzCgHqqkrUmxffRZvgsi';
    let redirect_uri = 'http://snapnews.cdc.gov.tw/account/profile/update_line_api_key/';
    window.location.href = 'https://notify-bot.line.me/oauth/authorize?scope=notify&response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&state=000'
};
