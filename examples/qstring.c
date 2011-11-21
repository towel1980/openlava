#include <stdio.h>
#include <string.h>
#include <sys/types.h>

static char *
gimmestr(char *s)
{
    static char buf[32];
    char *p;

    p = buf;
    if (s[0] == '"'
        && s[1] == '"')
        return NULL;

    ++s;
    while (*s != '"')
        *p++ = *s++;

    *p = 0;
    return buf;
}

int
main(int argc, char **argv)
{
    FILE *fp;
    char p[32];
    char p0[32];
    char p1[32];
    char *s;

    memset(p, 0, 32);
    memset(p0, 0, 32);
    memset(p1, 0, 32);

    fp = fopen("myfile", "r");
    while (fscanf(fp, "%s%s%s", p, p0, p1) != EOF)
        printf("%s %s %s\n", p, p0, p1);
    fclose(fp);

    memset(p, 0, 32);
    memset(p0, 0, 32);
    memset(p1, 0, 32);

    fp = fopen("myfile", "r");
    while (fscanf(fp, "%s", p) != EOF) {
        s = gimmestr(p);
        if (s)
            printf("%s\n", s);
        else
            printf("\"\"\n");
    }
    fclose(fp);

    printf("%d\n", sizeof(time_t));
    return 0;
}
