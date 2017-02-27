<?php
require_once 'simple_html_dom.php';

define('URL', 'http://blog.nogizaka46.com/');

date_default_timezone_set('Asia/Tokyo');

// HTTP通信
$html = file_get_html(URL);
$h1 = $html->find('h1');


// sqliteへの接続
try{
  // 接続
  $db = new PDO('sqlite:/home/shun/renoblog/entry.db');

  // SQL実行時にエラーの代わりに例外を投げるよう
  $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  // デフォルトのフェッチモードを連想配列に
  $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

  // 挿入
  foreach ($h1 as $id => $item) {
    $author =  $item->find('span.author',0)->plaintext;
    $title =  $item->find('span.entrytitle a',0)->plaintext;
    $url =  $item->find('span.entrytitle a',0)->href;
    try{
    $stmt = $db->prepare('INSERT INTO entry(auth, title, url) values (?, ?, ?)');
    $stmt->execute([$author, $title, $url]);
    echo 'runtime' . Date('Y/m/d H:i:s') . PHP_EOL;
    echo 'author : ' . $author . PHP_EOL;
    echo 'title  : ' . $title . PHP_EOL;
    echo 'url    : ' . $url . PHP_EOL;
    }
    catch(exception $e) {
    }
  }

} catch (exception $e) {
}
?>
