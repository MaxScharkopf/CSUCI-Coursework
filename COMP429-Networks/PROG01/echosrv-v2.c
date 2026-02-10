/*
* Kevin Scrivnor
* Copyright (C) 2024
* COMP 429 - Computer Networking
*
* A concurrent echo server
*/


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/wait.h>

#define PORT 9001
#define BACKLOG 10
#define BUF_SIZE 4096
#define MAX_CLIENTS 10

int sockfd;     
int total_clients = 0;

void quit(int);
void sub_client(int);
void handle_request(int, struct sockaddr_in*); 


int
main(int argc, char** argv)
{
    // on ctrl-c, quit
    signal(SIGINT, quit);
    // TODO: setup a signal handler for when the child process exits on SIGCHLD
    signal(SIGCHLD, sub_client);

    /* 
        Parameter description: socket(domanin (IPv4), socket type (stream. i.e we care), protocol (default for us is 0))
        The return value should be a file descriptor similar to fopen()
    */
    sockfd = socket(AF_INET, SOCK_STREAM, 0); 

    // if not 0 we have a problem
    if(sockfd < 0) {
        perror("Problem with socket()");
        exit(EXIT_FAILURE);
    } 


    struct sockaddr_in sa = {
        .sin_family = AF_INET,       // 32 bit address family IPv4
        .sin_port = htons(PORT),     // 16 bit port number 9001 (big-endian)
        .sin_addr = htonl(INADDR_ANY)     // 32 bit value address
    };
    /* 
        Parameter description: bind(sockfd (file descriptor), *addr (assigns address), addrlen(size in bytes of the address))
        Return 0 on succuss -1 on failrue
    */
    if(bind(sockfd, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
        perror("Problem with bind()");
        exit(EXIT_FAILURE);
    }

    if(listen(sockfd, BACKLOG) < 0) {
        perror("Problem with listen()");
        exit(EXIT_FAILURE);
    }

    int port = ntohs(sa.sin_port); // network 16 bit port number
    char ip[INET_ADDRSTRLEN];
    if(inet_ntop(AF_INET, (struct sockaddr*) &sa.sin_addr, ip, INET_ADDRSTRLEN) == NULL) {
        fprintf(stderr, "Couldn't convert server address\n");
    } else {
        printf("Listening on %s:%d\n", ip, port);
    }

    for(;;) {
        struct sockaddr_in* clia = malloc(sizeof(struct sockaddr_in)); // client address
        socklen_t addrlen = sizeof(struct sockaddr_in);                // address length
        int clifd = accept(sockfd, (struct sockaddr*) clia, &addrlen); // client file descriptor line of communication socket
        if(clifd < 0) {
            perror("Problem with accept()");
            continue;
        }

        // TODO: fork a child process if there is still room for clients
        //       call the handle_request function for the child process
        if(total_clients >= MAX_CLIENTS) {
            printf("Server is full with %d/%d sowwy :(\n", total_clients, MAX_CLIENTS);
            free(clia);
            close(clifd);
            continue;
        }

        int id = fork();
        if(id < 0){
            perror("fork");
            close(clifd);
            free(clia);
            continue;
        }
        if (id == 0){
            handle_request(clifd, clia);
        } 
        if(id > 0){
            total_clients++;
            printf("Client connected: %d/%d\n", total_clients, MAX_CLIENTS);
            close(clifd); // close socket
            free(clia);
            continue;
        }
    }
}

void
quit(int signo) 
{
    printf("Shutting down server...\n");
    // if ctrl-C is given
    close(sockfd); // close listening socket
    exit(EXIT_SUCCESS);
}

void
sub_client(int signo)
{
    while(waitpid(-1, NULL, WNOHANG) > 0) {
        
        total_clients--;
        printf("\nChild killed, client disconnected %d/%d\n", total_clients, MAX_CLIENTS);
    }
}

void
handle_request(int clifd, struct sockaddr_in* clia)
{
    // TODO: handle the request, echoing back to the client what they enter
    //       exit() when done to send SIGCHLD back to parent
    char buf[BUF_SIZE]; // array for data
    ssize_t numRead; 

    /*
        read(clifd(client to read from), buf(where to store data), BUF_SIZE(max bytes to read))
        store the value into numRead which could be how many bytes were read 
    */
    while((numRead = read(clifd, buf, BUF_SIZE)) > 0){ // keep reading until client leaves
        /*
        write(clifd(client to read from), buf(where to store data), BUF_SIZE(max bytes to read))
        */
        if(write(clifd, buf, numRead) != numRead){
            fprintf(stderr, "Could not perform write()");
            break;
        }
    }

    close(clifd); // close accept socket for this child
    free(clia);
    exit(EXIT_SUCCESS); 
}