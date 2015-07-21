# archivematica-pbcore
Adds support for Pbcore format for metadata cvs imports.

<h2>Install </h2>
Just replace these files<br>
/usr/lib/archivematica/MCPClient/clientScripts/archivematicaXMLNamesSpace.py<br>
/usr/lib/archivematica/MCPClient/clientScripts/archivematicaCreateMETS2.py<br>
then restart apache<br>
/etc/init.d/apache2 restart<br>


<h2>Instructions for importing</h2>
https://www.archivematica.org/en/docs/archivematica-1.4/user-manual/transfer/import-metadata/#import-metadata<br>

Your metadata.cvs should contain pbcore elements in the first row<br>
http://pbcore.org/elements/<br>
example: pbcore.title,pbcore.subject,etc<br>


<h2>Know issues</h2>
This script only supports main elements<br> 
sub-elements such as "essenceTrackType" will not be nested.


