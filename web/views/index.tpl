<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta content="text/html" charset="UTF-8">
  <link rel="stylesheet" href="static/css/bootstrap.css">
  <script src="static/js/jQuery.js"></script>
  <script src="static/js/bootstrap.js"></script>
  <script src="static/js/main.js"></script>
  <!--
  -->
</head>
<body>
<!--
  <div>
    <h2>Network</h2>
    <div></div>
    <embed src="/api?type=n&b=1&unit=H" type="image/svg+xml" width="500" height="200"></embed>
  </div>
  <div>
    <h2>Cpu</h2>
    <embed src="/api?type=c&b=1&unit=H" type="image/svg+xml" width="500" height="200"></embed>

  </div>
  <div>
    <h2>Memory</h2>
    <embed src="/api?type=m&b=1&unit=H" type="image/svg+xml" width="500" height="200"></embed>
  </div>
-->

  <div class="panel panel-default">
    <div class="panel-heading">
      <h1 class="panel-title">CPU</h1>
    </div>
    <div class="panel-body">
      <div class="btn-group">
        <button type="button" class="btn btn-default tag-cpu tag-15m">15分钟</button>
        <button type="button" class="btn btn-default tag-cpu tag-1h">1小时</button>
        <button type="button" class="btn btn-default tag-cpu tag-1d">1天</button>
        <button type="button" class="btn btn-default tag-cpu tag-7d">7天</button>
        <button type="button" class="btn btn-default tag-cpu tag-30d">30天</button>
      </div>
      <div>
        <img id="img-cpu" src="/api?type=c&b=1&unit=H"/>
      </div>
    </div>
  </div>

  <div class="panel panel-default">
    <div class="panel-heading">
      <h1 class="panel-title">网络</h1>
    </div>
    <div class="panel-body">
      <div class="btn-group">
        <button type="button" class="btn btn-default tag-network tag-15m">15分钟</button>
        <button type="button" class="btn btn-default tag-network tag-1h">1小时</button>
        <button type="button" class="btn btn-default tag-network tag-1d">1天</button>
        <button type="button" class="btn btn-default tag-network tag-7d">7天</button>
        <button type="button" class="btn btn-default tag-network tag-30d">30天</button>
      </div>
      <div>
        <img id="img-network" src="/api?type=n&b=1&unit=H"/>
      </div>
    </div>
  </div>
<div class="panel panel-default">

    <div class="panel-heading">
      <h1 class="panel-title">内存</h1>
    </div>
    <div class="panel-body">
      <div class="btn-group">
        <button type="button" class="btn btn-default tag-memory tag-15m">15分钟</button>
        <button type="button" class="btn btn-default tag-memory tag-1h">1小时</button>
        <button type="button" class="btn btn-default tag-memory tag-1d">1天</button>
        <button type="button" class="btn btn-default tag-memory tag-7d">7天</button>
        <button type="button" class="btn btn-default tag-memory tag-30d">30天</button>
      </div>
      <div>
        <img id="img-memory" src="/api?type=m&b=1&unit=H">
      </div>
    </div>
  </div></body>
</html>