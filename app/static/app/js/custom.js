jQuery(document).ready(function($) {
	// $('#post-it').click(function(){
	// 	VK.Api.call('wall.post', {access_token: "3f4806de0469ec539117b41e84524baf22b8926b3b886e6da459aabfbd51aadb3422da11fe967dd33d024", message: "123"}, function(r) {
	// 		if(r.response) {
	// 			$.post('', JSON.stringify({code: promo_code, method: 'create_post', attached_users: users_list}), function(response) {})
	// 		}
	// 	});
	// });
});
	VK.init({
        apiId: 5571721
    });
	function wall_post(token) {
 		var users_list = $('#friends-list').serializeArray();
 		if(users_list) {
	 		promo_code = '';
	 		message = 'Привет!\n';
	 		users_list.forEach(function(i, idx, array) {
			    message += '@id' + i.value;
			    if(idx != array.length - 1) message += ', ';
			});
	 	  	VK.Api.call('wall.post', {access_token: token, message: message}, function(r) {
				if(r.response) {
					$.post('', JSON.stringify({code: promo_code, method: 'create_post', attached_users: users_list}), function(response) {})
					//console.log('Сообщение отправлено! ID сообщения: ' + r.response.post_id);
				} else {
					//console.log('Ошибка! ' + r.error.error_code + ' ' + r.error.error_msg);
				}
			});
		}
    }