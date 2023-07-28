analysis a log and create a report for current logged users <br>

**The following are the exaple logs:**

*  '2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan',
*  '2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan',
*  '2020-01-21 18:53:21', 'login', 'webserver.local', 'lane',
*  '2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan',
*  '2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan',
*  '2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris',
<br>

Expected result: webserver.local: lane <br>
Explanation: Because only lane is currently logged into the webserver.local machine but not logout yet
