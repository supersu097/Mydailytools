#!/usr/bin/env bash
#set -o errexit


usernames='{{.usernames}}'
sudo='{{.sudo}}'

fail_user=()
for username in ${usernames[@]}
do

if [ -f key_repo/${username} ];then
#    if [ `cat key_repo/${username} | cut -d ' ' -f 1` = 'ssh-rsa' ];then

        if [[ ${sudo} == "True" ]]; then
            /usr/sbin/useradd -s /bin/bash  -m -d /home/${username} -G sudo ${username}
        elif [[ ${sudo} == "False" ]]; then
            /usr/sbin/useradd -s /bin/bash -m -d /home/${username} ${username}
        fi
  
        if [[ $? -ne 0 ]]; then
            echo -e "\nadd user error: ${username}\n"
            echo -e "=========================================="
            fail_user+=${username}
        else
            echo -e "\nThe username of ${username}'s pubkey file  detected!"
            mkdir -p -v /home/${username}/.ssh
            cat key_repo/${username} > /home/${username}/.ssh/authorized_keys
            chown -R -v ${username}:${username} /home/${username}/.ssh
            chmod 700 -v /home/${username}/.ssh
            chmod 600 -v /home/${username}/.ssh/authorized_keys
            echo -e "\nadd user and do other action successfully: ${username}\n"
            echo -e "=========================================="
        fi
    #else
    #    echo -e "\npls check the declaration of the pubkey's protocal you insert!"
    #    echo -e "=========================================="
    #    fail_user+=${username}
    #fi
    
else
    echo -e "\nThe username of '${username}' you passed do not exist in "
    echo -e "dir of 'key_repo',pls have a check!\n"
    echo -e "=========================================="
    fail_user+=${username}
fi

done

if [ ${#fail_user[@]} -ne 0 ];then
    echo 'one or more users adding failed is shown as below:'
    for i in ${fail_user}
    do
       echo "$i"
       echo
    done
    exit 1
fi
