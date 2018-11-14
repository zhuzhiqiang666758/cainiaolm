$(function(){
    $('form p').addClass('row form-group');
    $('form label').addClass('label-control col-sm-2 text-right').css('line-height','34px');
    $('form input[type="text"],input[type="password"],select,input[type="email"]').addClass('form-control col-sm-8').css('width','200px');
    $('form input[type="checkbox"]').css({'width':'34px','margin-top':'10px'});
    $('form span').addClass('col-sm-3').css({'width':'200px','color':'red','font-weight':'bold'});
    $('textarea').removeAttr('required');
    // $('form input').attr('onkeydown','if(event.keyCode==13) return false;')
    $('form input[type="text"]').attr('onkeypress','if(event.keyCode==13) return false')
    $('form input[type="file"]').addClass('form-control').width('200px');
});


