 
$(function(){

     //使用Ajax进行登录
     $('#kaka').blur(function () {
        // console.log(1)

         var data = $('#kaka').val()
         rest = {'phone':data}
         $.get('/check/',rest,function (response) {
             console.log(response)
             // console.log(2)
             if (response == '0') {
                 $('#abc').html('')
                 console.log(1)
             }else{
                 $('#abc').html('电话不正确')
             }

         })


     })

    $('#submit').click(function (event) {
        var phone = $('#phone').val()
        var password = $('#password').val()

        data = {
            'phone':phone,
            'password':password
        }

        $.get('/1check/',data,function (response) {
            console.log(response)
            event.preventDefault()


        })


    })




})
