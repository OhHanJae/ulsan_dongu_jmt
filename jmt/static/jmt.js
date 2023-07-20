$(document).ready(function(){
    $('#num_1').css('backgroundColor', '#2563eb')
    $('#town_all').css('backgroundColor','#2563eb')
})

$('.town').click(function(){
    var town = this.id.split('_')[1];

    switch(town){
        case 'all' :
            $('.town').css('backgroundColor', '#1e293b')
            $('#town_all').css('backgroundColor','#2563eb')
            break

        case 'del' : 
            $('.town').css('backgroundColor', '#1e293b')
            break

        default:
            $('#town_all').css('backgroundColor','#1e293b')
            if($('#town_' + town).css('backgroundColor') == 'rgb(37, 99, 235)'){
                $('#town_' + town).css('backgroundColor','#1e293b')//원래 색
            }else{
                $('#town_' + town).css('backgroundColor','#2563eb')//파란색
            }
    }
})

$('.num').click(function(){
    $('.num').css('backgroundColor', '#1e293b')
    $('#'+this.id).css('backgroundColor', '#2563eb')
})

$('#search').click(function(){
    var townAray = [];
    var numsAray = 0;

    const towns = document.querySelectorAll('.town')
    const nums = document.querySelectorAll('.num')

    towns.forEach(value => {
        var town = value.id.split('_')[1]
        if($('#town_' + town).css('backgroundColor') == 'rgb(37, 99, 235)'){
            townAray.push(town)
        }
    });

    nums.forEach(value => {
        var num = value.id.split('_')[1]
        if($('#num_' + num).css('backgroundColor') == 'rgb(37, 99, 235)'){
            numsAray = num
        }
    });

    $.ajax({
        url: "jmt/get_result",
        type: 'GET',
        data: {
            "towns": townAray,
            "num": numsAray
        },
        datatype: 'json',
        traditional : true,
        success: function (data) {
            var yes = document.getElementById('resultBoard')
            var result = data['read_data'];

            yes.removeChild(yes.firstChild);
            for (var i in result) {
                var name = result[i].name;
                var adress = result[i].adress;
                if(i==0){
                    var yess = "<div><p>가게 이름 : "+name+"</p><p>주소 : "+adress+"</p></div>"
                }else{
                    yess = yess + "<div><p>가게 이름 : "+name+"</p><p>주소 : "+adress+"</p></div>"
                }
            }
            yes.innerHTML = yess
        },
        error: function (request, status, error) {
        },
        complete: function () {
        }
    });
})

$('#close').click(function(){
    $('#readme').css("display","none");
})