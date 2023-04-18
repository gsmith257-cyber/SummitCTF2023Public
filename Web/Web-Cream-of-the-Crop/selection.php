<html>
<body>
<?php
if(isset($_POST['data'])) {
$xml = base64_decode($_POST['data']);
libxml_disable_entity_loader(false);
$dom = new DOMDocument();
$dom->loadXML($xml, LIBXML_NOENT | LIBXML_DTDLOAD);
$icecream = simplexml_import_dom($dom);
}
?>
<?php
echo $xml . "<br />";
echo "Anonymous likes " . $icecream->flavor;
$flavortown = $icecream->flavor;
file_put_contents('icecreamlogger.txt', "User enjoys the delights of ". $flavortown . " icecream!");
 ?>
</body>
</html>
