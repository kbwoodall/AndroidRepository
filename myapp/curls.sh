#!/bin/bash
#--------------------------------------------------------------------------
echo sending file
# //--------------------------------------------------------------------------
# list files
#curl ftp://myftpsite.com --user myname:password   
#--------------------------------------------------------------------------
# download file
curl -o stuff.txt ftp://appdev01.stephensmedia.com --user kwoodall:kwood09@3    
#curl -o getId ftp://appdev01.stephensmedia.com/bin --user kwoodall:kwood09@3    
#--------------------------------------------------------------------------
# upload file
#curl -T getId.txt ftp://appdev01.stephensmedia.com --user kwoodall:kwood09@3    
#curl -T getId.txt ftp://appdev01.stephensmedia.com/bin/ --user kwoodall:kwood09@3    
#--------------------------------------------------------------------------
#curl http://projects.reviewjournal.com/data/test/index11.php --user django:Wh|+3Sp@<3   
#--------------------------------------------------------------------------
#curl -X PUT -T /Users/kwoodall/myapp/newmobile.png -D - \
     #-H "ETag: 805120ec285a7ed28f74024422fe3594" \
     #-H "Content-Type: image/png" \
     #-H "X-Auth-Token: fc81aaa6-98a1-9ab0-94ba-aba9a89aa9ae" \
     #-H "X-Object-Meta-Screenie: Mel visits Outland" \
     #https://876552226582264:vAIdVdyFhfT_4Zb1iAZORNyQxLs@api.cloudinary.com/v1_1/lcbklf5b3/image/upload/newmobile.png
     #https://storage.clouddrive.com/v1/CF_xer7_343/images/wow1.jpg
#--------------------------------------------------------------------------
#
