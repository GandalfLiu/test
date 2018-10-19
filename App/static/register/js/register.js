

$(function(){
	
	//使用Ajax进行注册
    // console.log('哈哈')
    var reg1 = /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/

    // 验证电话格式
    $('#phone').blur(function () {
        $phone = $('#phone').val()
        var result = reg1.test($phone)
        if (result) {
            $('#haha').html('')
        }
        else{
            $('#haha').html('电话格式不正确')
        }
    })

    // 验证密码格式
    $('#password').blur(function () {
        var password1 = $('#password').val()
        if (password1.length < 6) {
            $('#hehe').html('密码格式不正确')

        }else{
            $('#hehe').html('')
        }


    })

    // 验证两次密码是否一致
    $('#password2').blur(function () {
        var password1 = $('#password').val()
        var password2 = $('#password2').val()
        if (password1 == password2) {
            $('#oo').html('')
        }else{
            $('#oo').html('两次密码不一致')
        }
    })


    // ajax验证帐号是否电话是否存在

    $('#phone').blur(function (event) {
        var phone = $('#phone').val()
        data = {'phone':phone}
        $.getJSON('/checkuser/',data,function (response) {
            // console.log(response)
            if (response == '0') {
                $('#qqq').html('电话已经存在')
                console.log(1)

            }else {
                $('#qqq').html('')
                console.log(2)
            }
        })

    })




	
})
