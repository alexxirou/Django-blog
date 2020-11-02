# Django-blog
Django configuration for  a small site serving static and dynamic content. 
Static files are handled by the same server using the middleware Whitenoise making it an ideal conifguration for small server setups as 
the actual pushing of the file down the network interface is handled by the kernel’s very efficient sendfile syscall, not by Python, making Whitenoise a pretty efficient solution.

