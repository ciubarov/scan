jQuery(document).ready(function($) {
    // По клику на лейбл отмечаем чекбокс и добавляем класс, для стилизации отмеченной фотографии
    $('#friends-list label').on('click', function (event) {
        event.preventDefault();
        var $check = $(':checkbox', this);
        $check.prop('checked', !$check.prop('checked'));
        $(this).toggleClass('active');
        var checked = $("#friends-list input:checked").length > 0;
	    if (!checked){
	        $('#friends-list button').addClass('nactive');
	    } else {
	    	$('#friends-list button').removeClass('nactive');
	    }
    });

    // Отмечаем всех друзей
    $('.check-all').on('click', function(){
    	console.log('1');
    	$('#friends-list label').each(function(){
    		$(this).addClass('active');
    	});
    	$('#friends-list input:checkbox').each(function(){
    		$(this).prop('checked', true);
    	});
    	$('#friends-list button').removeClass('nactive');
    	$(this).html('Снять выбор');
    	// Если все друзья отмечены, и клик призошёл по кнопку "Снять выбор", снимаем выбор со всех и меняем надпись
    	if($(this).hasClass('active')) {
	    	if(confirm("Вы уверены, что хотите отменить выбор?")) {
		    	$('#friends-list label').each(function(){
		    		$(this).removeClass('active');
		    	});
		    	$('#friends-list input:checkbox').each(function(){
		    		$(this).prop('checked', false);
		    	});
		    	$(this).html('Выбрать всех');
		    	$(this).removeClass('active');
		    	$('#friends-list button').addClass('nactive');
	    	}
	    } else {
	    	$(this).addClass('active');
	    }
    });
});
VK.init({
    apiId: 5571721
});
function wall_post(token,post_text) {
		var users_list = $('#friends-list').serializeArray();
		if(users_list) {
 		promo_code = '';
 		count = 0;
 		message = post_text + '\n';
 		users_list.forEach(function(i, idx, array) {
		    message += '@id' + i.value;
		    if(idx != array.length - 1) message += ', ';
		    count += 1;
		});
		if(count === 0) {
			alert('Вы должны выбрать хотя бы одного друга!');
		} else {
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
}