# archivematica-pbcore
Adds support for Pbcore format for metadata csv imports in to archivematic 1.4.1.<br>
https://github.com/artefactual/archivematica


<h2>Installation </h2>
Replace these files<br>
<pre><code>/usr/lib/archivematica/MCPClient/clientScripts/archivematicaXMLNamesSpace.py
/usr/lib/archivematica/MCPClient/clientScripts/archivematicaCreateMETS2.py
</code>
</pre>
then restart apache<br>
<pre><code>/etc/init.d/apache2 restart</code></pre>


<h2>Instructions for importing</h2>
https://www.archivematica.org/en/docs/archivematica-1.4/user-manual/transfer/import-metadata/#import-metadata<br>

Your metadata.csv should contain pbcore elements in the first row<br>
http://pbcore.org/elements/<br>
<pre><code>example: pbcore.title,pbcore.subject,etc</code></pre>


<h2>Limitations</h2>
This script only supports main elements<br> 
sub-elements such as "essenceTrackType" will not be nested.


