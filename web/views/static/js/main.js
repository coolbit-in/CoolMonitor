$(document).ready(function() {
    //$('img#img-network').load('/api?type=n&b=1&unit=H');
    //$('img#img-cpu').load('/api?type=c&b=1&unit=H');
    //$('img#img-memory').load('/api?type=m&b=1&unit=H');
    $('button.tag-15m.tag-network').click(function(){
        $.get('/api?type=n&b=15&unit=M', function() {
            $('img#img-network').attr('src','/api?type=n&b=15&unit=M')
        });
    });
    $('button.tag-1h.tag-network').click(function(){
        $.get('/api?type=n&b=1&unit=H', function() {
            $('img#img-network').attr('src','/api?type=n&b=1&unit=H')
        });
    });
    $('button.tag-1d.tag-network').click(function(){
        $.get('/api?type=n&b=1&unit=D', function() {
            $('img#img-network').attr('src','/api?type=n&b=1&unit=D')
        });
    });
    $('button.tag-7d.tag-network').click(function(){
        $.get('/api?type=n&b=7&unit=D', function() {
            $('img#img-network').attr('src','/api?type=n&b=7&unit=D')
        });
    });
    $('button.tag-30d.tag-network').click(function(){
        $.get('/api?type=n&b=30&unit=D', function() {
            $('img#img-network').attr('src','/api?type=n&b=30&unit=D')
        });
    });

    $('button.tag-15m.tag-cpu').click(function(){
        $.get('/api?type=c&b=15&unit=M', function() {
            $('img#img-cpu').attr('src','/api?type=c&b=15&unit=M')
        });
    });
    $('button.tag-1h.tag-cpu').click(function(){
        $.get('/api?type=c&b=1&unit=H', function() {
            $('img#img-cpu').attr('src','/api?type=c&b=1l&unit=H')
        });
    });
    $('button.tag-1d.tag-cpu').click(function(){
        $.get('/api?type=c&b=1&unit=D', function() {
            $('img#img-cpu').attr('src','/api?type=c&b=1l&unit=D')
        });
    });
    $('button.tag-7d.tag-cpu').click(function(){
        $.get('/api?type=c&b=7&unit=D', function() {
            $('img#img-cpu').attr('src','/api?type=c&b=7l&unit=D')
        });
    });
    $('button.tag-30d.tag-cpu').click(function(){
        $.get('/api?type=c&b=30&unit=D', function() {
            $('img#img-cpu').attr('src','/api?type=c&b=30l&unit=D')
        });
    });

    $('button.tag-15m.tag-memory').click(function(){
        $.get('/api?type=m&b=15&unit=M', function() {
            $('img#img-memory').attr('src','/api?type=m&b=15&unit=M')
        });
    });
    $('button.tag-1h.tag-memory').click(function(){
        $.get('/api?type=m&b=1&unit=H', function() {
            $('img#img-memory').attr('src','/api?type=m&b=1&unit=H')
        });
    });
    $('button.tag-1d.tag-memory').click(function(){
        $.get('/api?type=m&b=1&unit=D', function() {
            $('img#img-memory').attr('src','/api?type=m&b=1&unit=D')
        });
    });
    $('button.tag-7d.tag-memory').click(function(){
        $.get('/api?type=m&b=7&unit=D', function() {
            $('img#img-memory').attr('src','/api?type=m&b=7&unit=D')
        });
    });
    $('button.tag-30d.tag-memory').click(function(){
        $.get('/api?type=m&b=30&unit=D', function() {
            $('img#img-memory').attr('src','/api?type=m&b=30&unit=D')
        });
    });

});
