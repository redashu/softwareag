FROM  fedora
#  fedora is  base raw image of  docker 
MAINTAINER  ashutoshh@linux.com
#  dev info purpose
RUN  yum   install   httpd -y
#  this will install httpd web server in raw docker image
ADD  mywebapp  /var/www/html/
#  this is copy  code to docker image
EXPOSE 80
#  using  port  80  in docker image
ENTRYPOINT  ["httpd","-D","FOREGROUND"]
#  it will start  httpd  services
