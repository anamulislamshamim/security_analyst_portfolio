**I have to analysis the log and count the good and naughty users from the log for debugging our system** <br>
    The followings are some example log: The ouput should be like: {'good_user': 1, 'naughty_user': 3} <br>
    Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user) <br>
    Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006) <br>
    Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007) <br>
    Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user) <br>
    Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\" <br>
    Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user) <br>
    Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)