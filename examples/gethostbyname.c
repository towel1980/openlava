#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

struct hostent *hp;
struct in_addr a;

int
main (int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "usage: %s hostname\n", argv[0]);
        return 1;
    }
    hp = gethostbyname (argv[1]);
    if (hp) {

        printf("name: %s\n", hp->h_name);
        while (*hp->h_aliases)
            printf("alias: %s\n", *hp->h_aliases++);

        while (*hp->h_addr_list) {
            char * p;
            memcpy(&a, *hp->h_addr_list++, sizeof(a));
            p = inet_ntoa(a);
            printf("address: %s\n", inet_ntoa(a));
        }
    }

    return 0;
}

