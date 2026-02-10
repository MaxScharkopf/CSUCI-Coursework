
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 9001
#define ADDR "127.0.0.1"
#define BUF_SIZE 4096

int
main(int argc, char** argv){
    
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd < 0){
        printf("Failed to open socket");
        exit(EXIT_FAILURE);      
    }

    struct sockaddr_in sa = {
        .sin_family = AF_INET,
        .sin_port = htons(PORT),
        .sin_addr = inet_addr(ADDR)
    };

    if(connect(sockfd, (struct sockaddr*) &sa, sizeof(sa)) < 0){
        printf("Failed to conenct");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    char buf[BUF_SIZE];
    
    for(;;) {
       
        fgets(buf, BUF_SIZE, stdin);
        write(sockfd, buf, strlen(buf));
        read(sockfd, buf, BUF_SIZE - 1);
        printf("Server says: %s\n", buf);
    }

    

    close(sockfd);
}