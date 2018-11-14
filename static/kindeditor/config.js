KindEditor.ready(function(K) {
    //alert('kindeditor');//测试
        window.editor = K.create('textarea',{
            width:'100%',
            height:200,
            uploadJson:'/admin/upload/kindeditor'
        });
});